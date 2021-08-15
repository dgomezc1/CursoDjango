class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        #decimo que carro va a ser el diccionario carro que tiene la session
        self.carro = self.session.get("carro")
        #Si no hay un carro, se va a crear uno en la session
        if not self.carro:
            self.carro = self.session["carro"]={}
        #Si ya tenia carro entonces continuamos con ese
        
    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified = True

    def eliminar(self, producto):
        productoId = str(producto.id)
        if productoId in self.carro:
            del self.carro[productoId]
            self.guardar_carro()
        
    def restar_producto(self, producto):
        productoId = str(producto.id)
        for key, value in self.carro.items():
            if key == productoId:
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"]==0:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified = True
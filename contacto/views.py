from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contactos(request):
    formulario_contacto = FormularioContacto()
    if request.method == 'POST':
        formulario_contacto=FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            Email = EmailMessage("Mensaje desde app DJANGO", "El usuario con nombre {} con la direccion {} te escribe lo siguiente:\n\n {}".format(nombre, email, contenido),"",["dgomezcorrea10@gmail.com"],reply_to=[email])
            try:
                Email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?noValido")
    return render(request,"contacto/contacto.html", {'miFormulario': formulario_contacto})

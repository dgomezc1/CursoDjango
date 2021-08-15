from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

#Registro de los modelos
admin.site.register(CategoriaProd, CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
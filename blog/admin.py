from django.contrib import admin
from django.db import models
from .models import Categoria, Post

# Register your models here.

#Clase para declarar lo que no queremos que lea
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

#Registro de los modelos en el admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
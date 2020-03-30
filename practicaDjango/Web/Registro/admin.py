from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Usuarios,Registros
# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Registros)
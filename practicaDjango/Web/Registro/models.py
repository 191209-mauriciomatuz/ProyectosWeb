from django.db import models

# Create your models here.
class Registros(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 254, blank = False, null = False)
    correo = models.CharField(max_length = 254, blank = False, null = False)
    password = models.CharField(max_length = 254, blank = False, null = False)


        
    class Meta:
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.CharField(max_length = 254, blank = False, null = False)
    password = models.CharField(max_length = 254, blank = False, null = False)
    registro_id = models.ForeignKey(Registros, on_delete= models.CASCADE)
    
    
    class Meta:
        ordering = ['usuario']
    
    def __str__(self):
        return self.usuario
from django import forms
from .models import Registros

class registroFrom(forms.ModelForm):
    class Meta:
        model = Registros
        #campos que seran rellenados para registrar
        fields =['nombre','correo','password']
        
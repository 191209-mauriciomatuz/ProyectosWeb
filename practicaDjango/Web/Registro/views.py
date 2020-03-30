from django.shortcuts import render
from django.shortcuts import redirect
from .forms import registroFrom
from Landing import views


# Create your views here.
def registro(request):
    return render(request,'landing')


def post(request):
    if request.method == 'POST':
        registro_form = registroFrom(request.POST)
        if registro_form.is_valid():
            registro_form.save()
            return redirect('inicia')
    else:
        registro_form = registroFrom()
      
    return render(request,'Registro/Registro.html',{'registro_form':registro_form})






















#AGREGAR AL DE GRIMALDO 
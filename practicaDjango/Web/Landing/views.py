from django.shortcuts import render
#invoco estas 3 librerias 
from django.views.generic import View
from django.shortcuts import redirect

#realizo cada clase para html 
class LandingClass(View):
    tamplateOK = 'Landing/Landing.html'
    def get(self,request,*args,**kwargs):
        return render(request,'Landing/Landing.html') # retorno la direcion de la carpeta para cada html
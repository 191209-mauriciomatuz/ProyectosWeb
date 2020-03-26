from django.shortcuts import render
#invoco estas 3 librerias 
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate


class LoginClass(View):
    template = 'Login/Login.html'
    def get(self,request,*args,**kwargs):
        print("lo siento chavo")
        return render(request,self.template,{})
    
    def post(self,request,*args,**kwargs):
        users = request.POST['user']
        password = request.POST['password']
        user = authenticate(username =users, password = password)

        if user is not None:
            return redirect('Dashboard:Dashboard') ## me redirigo en la urls de dashboard
        else:
            self.messege = 'no existe ese usuario o contraseña'
            
        return render(request,self.template,self.get_context())

    def get_context(self):
        return{
            'error':self.messege
        }
    



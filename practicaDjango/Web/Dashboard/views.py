from django.shortcuts import render
#invoco estas 3 librerias 
from django.views.generic import View
from django.shortcuts import redirect


class DashboardClass(View):
    def  get(self,request,*args,**kwargs):
        return render(request,'Dashboard/dashboard.html')


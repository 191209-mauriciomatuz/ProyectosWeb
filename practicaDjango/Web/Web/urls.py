
from django.contrib import admin
from django.urls import  include,path,re_path
from Login import views #importo o invoco el arhivo
from Landing import views
from Dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/',include('Login.urls')), #invoco el url hija
    path('',include('Landing.urls')),
    path('Dashboard/',include('Dashboard.urls')),
]


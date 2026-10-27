from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.iniciar_usuario, name='login'),
    path('inicio/',views.inicio, name= 'inicio'),
    path('registro/', views.registro, name='registro'),
    path('guia/', views.guia, name='guia'),
    path('desarrollo/', views.desarrollo, name='desarrollo'),
]
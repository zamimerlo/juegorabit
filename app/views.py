from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def inicio(request):
    return render (request, "app/inicio.html")

def registro(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        usuario = request.POST.get("usuario")
        contrasenia = request.POST.get("contrasenia")
        gmail = request.POST.get("gmail")
        
        if User.objects.filter(username=usuario).exists():
            return render(request, "app/registro.html", {
                "mensaje": "El nombre de usuario ya está registrado."
            })

        if User.objects.filter(email=gmail).exists():
            return render(request, "app/registro.html", {
                "mensaje": "El correo electrónico ya está en uso."
            })
            
        User.objects.create_user(
            username=usuario,
            email=gmail,
            password=contrasenia,
            first_name=nombre,
            last_name=apellido
        )

        return render(request, "app/registro.html", {
            "exito": "Te registraste con éxito"})

    return render(request, "app/registro.html")

def iniciar_usuario(request):
    if request.method == "POST":
        username =request.POST["username"]
        password=request.POST["password"]
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render( request, "app/inicio.html",{"usuario": user})
        else: 
            return render (request, "app/login.html", {"mensaje": "Usuario o contraseña incorrectas"})
    return render (request, "app/login.html")


def guia(request):
    return render (request, "app/guia.html")
def desarrollo(request):
    return render (request, "app/desarrollo.html")

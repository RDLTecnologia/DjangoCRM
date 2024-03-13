from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
   
    if ( request.method == "POST"):
        userName = request.POST['username']
        userPassword = request.POST['password']
        
        userAuth = authenticate(request, username=userName, password=userPassword)
        
        if ( userAuth is not None ):
            login(request, userAuth)
            messages.success(request, "Você está logado")
            return redirect('home')
        else:
            messages.error(request, "User Name or Password not correct !")
            return redirect('home')        
    else:        
        return render(request, 'home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "Você foi deslogado !!")
    return redirect('home')
 
def register_user(request):
    return render(request, 'register.html', {})
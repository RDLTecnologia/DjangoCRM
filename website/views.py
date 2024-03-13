from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    
    records = Record.objects.all()
   
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
        return render(request, 'home.html', {'records': records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "Você foi deslogado !!")
    return redirect('home')
 
def register_user(request):
    if ( request.method == "POST"):
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                # Autentica e Loga
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You Have Register !!!")
                return redirect('home')
    else:
        form = SignUpForm()               
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if ( request.user.is_authenticated ):
        if ( pk is not None ):
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Você deve estar logado para acessar essa página")
        return redirect('home')
    
    
def delete_record(request, pk):
    if ( request.user.is_authenticated ):
        if ( pk is not None ):
            delete_it = Record.objects.get(id=pk)
            delete_it.delete()
            messages.success(request, "Registro excluído com sucesso !!!")
            return redirect('home')
    else:
        messages.success(request, "Você deve estar logado para acessar essa página")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if ( request.user.is_authenticated ):
        if ( request.method == "POST" ):
            if ( form.is_valid() ):
                add_record = form.save()
                messages.success(request, "Registro inserido com sucesso !!!")
                return redirect('home')
            
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Você deve estar logado para acessar essa página")
        return redirect('home')
    
def update_record(request, pk):
    if ( request.user.is_authenticated ):
        current_record = Record.objects.get(id=pk)        
        form = AddRecordForm(request.POST or None, instance=current_record)
        if ( form.is_valid() ):
            form.save()
            messages.success(request, "Registro atualizado com sucesso")
            return redirect('home')
        
        return render(request, 'update_record.html', {'form': form })
    else:
        messages.success(request, "Você deve estar logado para acessar essa página")
        return redirect('home')
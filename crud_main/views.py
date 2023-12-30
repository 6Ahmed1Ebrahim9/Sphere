from django.shortcuts import render, redirect
from .forms import CreateUserForm, Loginform
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    return render(request, 'crud_main/landing.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save() 
            return redirect('login')
            
    context = {'register_form': form}
    
    return render(request, 'crud_main/register.html', context)


# Login View

def login(request):
    form = Loginform()
    
    if request.method == 'POST':
        form = Loginform(request.POST) 
        
        if form.is_valid():
            
            username = request.POST.get('username')
            
            password = request.POST.get('password')
            
            user = authenticate(
                request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
            
                # return redirect('')
        
    context = {'login_form': form}
    
    return render(request, 'crud_main/login.html', context)


# Logout View

def logout(request):
    auth.logout(request)
    return redirect('login')

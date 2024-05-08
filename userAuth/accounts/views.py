from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, 'register.html', {'error_message': error_message})

        
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, 'register.html', {'error_message': error_message})

        
        if User.objects.filter(email=email).exists():
            error_message = "Email already exists."
            return render(request, 'register.html', {'error_message': error_message})

        
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            next_url = request.GET.get('next', 'app')
            return redirect(next_url)
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def home(request):
    if request.user.is_authenticated and request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'home.html', {'users': users})
    else:
        return render(request, 'home.html')
@login_required
def app(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = User.objects.all()
            return render(request, 'app.html', {'users': users})
        else:
            return render(request, 'app.html', {'user': request.user})
    else:
        return render(request, 'app.html')
def logout_view(request):
    logout(request)
    return redirect('home')

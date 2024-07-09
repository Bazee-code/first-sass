from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def login_view(request, *args, **kwargs):


    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        
        if all([username, password]):
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print('login here')
                return redirect('/')
        
    return render(request, 'auth/login.html',{})

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        username_exists = User.objects.filter(username__iexact = username).exists()
        email_exists = User.objects.filter(email__iexact = email)

        print('user exists',username_exists)
        print('email exists',email_exists)
        
        try:
            User.objects.create_user(username, email, password)
        except:
            pass
        
    return render(request,'auth/register.html',{})
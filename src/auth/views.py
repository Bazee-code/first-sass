from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate

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
import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import Visit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view (request, *args, **kwargs): 
    print('auth',request.user.is_authenticated)
    if(request.user.is_authenticated):
        print('first name',request.user.first_name)
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = Visit.objects.all()
    page_qs = Visit.objects.filter(path = request.path)
    my_title = 'Refreshing django'
    my_context = {
        "page_title" : my_title,
        "total_page_visits":qs.count(),
        "page_visits": page_qs.count()
    }
    html_templage = 'home.html'
    Visit.objects.create(path= request.path) #store our visits model data
    return render(request, html_templage,my_context)
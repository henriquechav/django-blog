from django.shortcuts import render
from .models import Posts

def index(request):
    posts = Posts.objects.all()
    data = {'posts': posts}
    return render(request, 'index.html', data)

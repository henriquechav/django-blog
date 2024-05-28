from django.shortcuts import render
from .models import Posts

def index(request):
    posts = Posts.objects.all()
    data = {'posts': posts}
    return render(request, 'index.html', data)

def post(request, pk):
    post = Posts.objects.get(id=pk)
    data = {'post': post}
    return render(request, 'post.html', data)

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context = {
    'title': 'Menu Blog',
    'subtitle': 'Welcome to my website',
    'developer': 'Venomare',
    'banner': 'blog/images/venomare.png',
    'css_apps': 'blog/css/styles_blog.css',
  }
  return render(request, 'blog/index.html', context)

def news(request):
  context = {
    'title': 'News',
    'developer': 'Venomare',
  }
  return render(request, 'blog/index.html', context)

def article(request):
  context = {
    'title': 'Article',
    'developer': 'Venomare',
  }
  return render(request, 'blog/index.html', context)

def search(request):
  return HttpResponse('This is menu search')
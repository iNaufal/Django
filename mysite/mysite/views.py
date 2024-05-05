from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context = {
    'title': 'Web development full stack',
    'subtitle': 'Welcome to my website',
    'developer': 'Venomare',
    'banner': 'images/venomare.png',
    # 'css': 'css/css_global.css',
  }
  return render(request, 'index.html', context)
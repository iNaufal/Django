from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context = {
    'title': 'web development full stack',
    'developer': 'Venomare',
  }
  return render(request, 'index.html', context)
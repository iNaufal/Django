from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context = {
    'title': 'Web development full stack',
    'subtitle': 'Welcome to my website',
    'developer': 'Venomare',
    'nav':[
      ['/','Home'],
      ['/blog','Blog'],
      ['/contact','Contact'],
    ]
  }
  return render(request, 'index.html', context)
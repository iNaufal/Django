from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'title': 'About Contact',
    'subtitle': 'Welcome to my website',
    'developer': 'Venomare',
    'banner':'contact/images/venomare.png',
  }
  return render(request, 'contact/index.html', context)
from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'title': 'About Contact',
    'subtitle': 'Welcome to my website',
    'developer': 'Venomare',
    'banner':'contact/images/vreedom.jpeg',
    'css_apps': 'contact/css/styles_contact.css',
  }
  return render(request, 'contact/index.html', context)
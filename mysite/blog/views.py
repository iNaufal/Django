from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'blog/index.html')

def search(request):
  return HttpResponse('This is menu search')
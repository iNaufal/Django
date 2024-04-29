from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def index1(request):
  str = "Testing\n"
  str1 = "testing2\n"
  str2 = "testing3\n"
  output = str + str1 +str2
  return HttpResponse(output)
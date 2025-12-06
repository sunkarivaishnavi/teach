from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("WELCOME TO TEACHER DATA HOME PAGE")
def clg(request):
    return render(request,'dashboard.html')

# Create your views here.

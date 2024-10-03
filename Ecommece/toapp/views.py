from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def registerview(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')
def submit(request):
    return render(request,'submit.html')
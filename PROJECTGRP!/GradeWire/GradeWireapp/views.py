from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def teacherLogin(request):
    return render(request,'teach_login.html')
def teacherRegister(request):
    return render(request,'teach_register.html')
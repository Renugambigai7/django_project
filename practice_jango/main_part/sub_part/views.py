from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def dashboard(request):
    return render(request,'dashboard.html')
   
def product(request):
    return render(request,'product.html')

def  customer(request):
    return render(request,'customer.html')

def register_form_submission(request):
   
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email_id=request.POST.get('email_id')
    password=request.POST.get('password')
    print(first_name,last_name,email_id,password)

    return render(request,'register.html')
    
    
    
   
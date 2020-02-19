from django.shortcuts import render, redirect
from django.http import HttpResponse as HTR
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



#the email validator function
def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
# Create your views here.
def posts_home(request):
    return render(request, 'shop/posts_home.html')

def home(request):
    return render(request, 'shop/home.html')

def shop(request):

    return render(request, 'shop/shop.html')

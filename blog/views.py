from django.shortcuts import render, redirect
from django.http import HttpResponse as HTR
from .forms import create_user, user_login_form
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import contact_form


#the email validator function
def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
# Create your views here.
def posts_home(request):
    return render(request, 'blog/posts_home.html')

def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    contact_us_form = contact_form
    return render(request, 'blog/contact.html',{'contact_form':contact_us_form})

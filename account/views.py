from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse as HTR
from .forms import create_user, user_login_form
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
    return render(request, 'account/posts_home.html')

def myaccount_home(request):
    return render(request, 'account/myaccount_home.html')
#create account function
def create_account(request):
    create_user_form = create_user
    return render(request, 'account/create_account.html',{'create_user_form':create_user_form})
#create account handler
def create_account_handler(request):
    create_user_form = create_user
    if request.method == 'POST':
        received_data = request.POST
        captured_data = create_user(received_data)
        if captured_data.is_valid():
            password1 = captured_data.cleaned_data.get('password')
            password2 = captured_data.cleaned_data.get('confirm_password')
            username = captured_data.cleaned_data.get('username')
            if validateEmail(captured_data.cleaned_data.get('email')):
                if password1 == password2:
                    user = authenticate(request,username = username, password = password1)
                    if user is not None:
                        msg = 'username already in use'
                        return render(request, 'account/create_account.html',{'create_user_form':create_user_form, 'msg':msg})
                    else:
                        user_create_init = captured_data.save(commit = False)
                        user_create_init.set_password(password1)
                        user_create_init.save()
                        return render(request, 'account/posts_home.html')  
                
                else:
                    msg = "passwords do not match"
                    return render(request, 'account/create_account.html',{'create_user_form':create_user_form, 'msg':msg})
            else:
                msg = "Invalid email"
                return render(request, 'account/create_account.html',{'create_user_form':create_user_form, 'msg':msg})
        else:
            msg = "Username already taken"
            return render(request, 'account/create_account.html',{'create_user_form':create_user_form, 'msg':msg})
    return HTR('create user handler')

#user login function
def user_login(request):
    login_form= user_login_form
    return render(request, 'account/user_login.html',{'login_form':login_form})

#user login handler function
def user_login_handler(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/blog/')
        else:
            login_form= user_login_form
            msg = "username or password incorrect"
            return render(request, 'account/user_login.html',{'login_form':login_form, 'msg':msg})
    
#the password reset function
def reset_password(request):
    return HTR('reset password')
#password reset handler function
def reset_password_handler(request):
    return HTR('reset password handler')
def user_logout(request):
    logout(request)
    return redirect('/blog/')

from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from . import forms
from django.core.mail import send_mail
import urllib.parse
from FPPMS.settings import EMAIL_HOST_USER


redirectUrl = 'http://127.0.0.1:8000/resetPassword?'    ##change link for the new password
appname= ''


def forgotpassword(request):

   return render(request, "authenticate/ForgotPassword.html")
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            messages.error(request,('Invalid Username or Password '))
            return redirect('login')
            
    else:
        return render(request,'authenticate/login.html',{})
        
def resetPassword(request):
    return render(request,'authenticate/resetPassword.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('You were logged out'))
    return redirect('login')

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = appname+'<IMP> : Password Reset Link'
        message = getMessageContent()
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'authenticate/login.html')
    return render(request, 'authenticate/ForgotPassword.html')


def getMessageContent():
    queryparam = { 'next' : '/admin/'}
    body = 'Please click on the below link to reset your password.\r\n{0}'.format(redirectUrl+urllib.parse.urlencode(queryparam))
    return body


from django.shortcuts import render,redirect,HttpResponse
# from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Application.models import *

def Home(request):
    return render(request, 'index.html')

def contact(request):
        if request.method == "POST":
            a = request.POST.get('name')
            b = request.POST.get('email')
            c = request.POST.get('phone')
            d = request.POST.get('message')
            enquiry = contact_table(name = a, email = b, phone = c, message = d)
            enquiry.save()
            
            messages.success(request,'Your form is sucessfully submitted')
        return render(request, 'contact.html')

def LOGIN(request):
    return render(request, 'login.html')

def login_i(request):
    return render(request, 'login_i.html')

def Help(request):
    return render(request, 'help.html')


def doLogin(request):

    # if request.method == 'POST':
    #     username=request.POST.get('email')
    #     password=request.POST.get('password')
    #     user = EmailBackEnd.authenticate(request,username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         user_type=user.user_type
    #         if user_type == 1:
    #             request.session['username_id'] = email 
    #             return HttpResponse('This is Tpo Panel')
    #         elif user_type=='2':
    #             return HttpResponse('This is Company Panel')
    #         elif user_type=='3':
    #             return HttpResponse('This is Student Panel')
    #         else:
    #             messages.error(request,'Email and Password Are invalid')
    #             return redirect('login')
    #     else:
    #         messages.error(request,'Email and Password Are invalid')
    #         return redirect('login')
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Homepage')
        else:
            messages.error(request, 'Incorrect username or password!..') 
            return redirect('login')  
        
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')

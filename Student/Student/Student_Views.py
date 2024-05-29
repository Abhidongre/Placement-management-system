from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages

def student_login(request):
    return render(request,'Student/student_login.html')

def doLogin1(request):
    
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_home')
        else:
            messages.error(request, 'Incorrect username or password!..') 
            return redirect('student login')  
        
    return render(request, 'login.html')

@login_required(login_url='student login')
def student_home(request):
    return render(request, 'Student/student_home.html')

def companies1(request):
    return render(request, 'Student/companies1.html')

def courses(request):
    return render(request, 'Student/courses.html')
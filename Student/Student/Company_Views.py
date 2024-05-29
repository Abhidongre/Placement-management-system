from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def Homepage(request):
    return render(request, 'Company/companyhome.html')

def student_info(request):
    return render(request, 'Company/studentinfo.html')

def contact1(request):
    return render(request, 'Company/contact1.html')


def Help1(request):
    return render(request, 'Company/Help1.html')

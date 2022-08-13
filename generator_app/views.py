from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator_app/home.html')

def password(request):

    characs = list('abcdefghijklmnopqrstuvwxyz')
    pwd = ''

    leng= int(request.GET.get('length'))
    if not(leng>=6 and leng<=14):
        leng=12
    if request.GET.get('uppercase'):
        characs.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characs.extend(list('!@#$%^&*()~`'))

    if request.GET.get('numbers'):
        characs.extend(list('0123456789'))


    for x in range(leng):
        pwd += random.choice(characs)
    return(render(request,'generator_app/password.html',{'password':pwd}))

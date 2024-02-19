from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse("Hello there friend")
    return render(request, 'generator/home.html', {'password': 'dkfjdkfb'})

def password(request):
    chars = list('qwertyuiopasdfghjklzxcvbnm')
    length = int(request.GET.get('length',9))
    uppercase =  request.GET.get('uppercase',"")
    numbers =  request.GET.get('numbers',"")
    specials =  request.GET.get('special',"")

    if uppercase:
        chars += "QWERTYUIOPASDFGHJKLZXCVBNM"
    
    if numbers:
        chars += "1234567890"
    
    if specials:
        chars += "!@#$%^&*()"

    password = ''

    for x in range(length):
        password += random.choice(chars)
    
    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, "generator/about.html") 
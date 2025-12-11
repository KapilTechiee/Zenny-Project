from django.shortcuts import render
from django.http import HttpResponse   #Edit by me
# Create your views here.

def say_hello(request):      #Edit by me
    return render(request,'index.html', {'name' : 'Kapil'})   #Edit by me
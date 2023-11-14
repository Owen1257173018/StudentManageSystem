from django.shortcuts import render,reverse
from django.http import request

# Create your views here.

def index(request):

    return render(request,'index.html')
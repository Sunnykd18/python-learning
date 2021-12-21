from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')


def contacts(request):
    # return HttpResponse('contact')  
    return render(request,'contact.html')     
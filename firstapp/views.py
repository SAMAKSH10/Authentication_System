from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def signup(request):
    # return render(request,"authentication/signup.html")
    pass
def signin(request):
   # return render(request,"authentication/signin.html")
    pass
def signout(request):
    pass
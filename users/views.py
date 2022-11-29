from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login, logout
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

from app.models import Account







def registerPage(request):
    pass
    # form = UserCreationForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            
    # context = {'form': form}
    # return render(request, 'users/register1.html', context)
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out"
    })


def resetpwd(request):
    return render(request,'users/reset_password.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['username']
            form.cleaned_data['email']
            form.cleaned_data['password1']
            form.save()
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/register.html', {
                'form': form
            })

    return render(request, 'users/register.html',{
            'form': RegistrationForm()
        })




    
    
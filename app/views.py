from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from .models import Account, Item, menuItem
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    
    return render(request,'app/index.html',{
        "items": Item.objects.all()
    })

def post(request):
    return render(request, 'app/postNews.html' )

# detail  information of the item
def item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, "app/item.html", {
        "item": item
    })

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'app/register1.html', context)

def update(request, user_id):
    user = Account.objects.get(id=user_id)
    context = {
        'user' : user
    }
    return render(request, 'users/update_information', context)

def updaterecord(request, user_id):
    fullname =request.POST['fullname']
    
    user = Account.objects.get(id=user_id)
    user.fullname = fullname
    user.save()
    
    return HttpResponseRedirect(reverse('indexApp'))


def get_type_item(request):
    
    type_post =["Newtopost", "new to find"]
    return render (request, 'postNews.html', {
        'typePost': ["Newtopost", "new to find"]
            })


def addItem(request):
    if request.method =='POST':
        title = request.POST['title']
        typepost = request.POST['typepost']
        typeitem = request.POST['typeitem']
        addrlost = request.POST['addresslost']
        fullname= request.POST['fullname']
        content = request.POST['content']
        address = request.POST['address']
        phonenumber = request.POST['phoneNum']
        email = request.POST['Email']
        image = request.POST['image']
    
        item = Item.objects.create(title=title, postInfo=typepost, typeItem=typeitem, adrLost=addrlost, image=image, content=content, fullname=fullname, address = address )
        
        if item:
            item.save()
            return HttpResponseRedirect(reverse('indexApp'))
        else:
            return render(request, 'app/error.html')
    return render(request, "app/postnew.html")
            
        
    
    
        
    
def introduce(request):
    return render(request,"app/introduce.html")
def terms(request):
    return render(request,"app/terms.html")
def policy(request):
    return render(request,"app/policy.html")
def donate(request):
    return render(request,"app/donate.html")
def warning(request):
    return render(request,"app/warning.html")
def report(request):
    return render(request,"app/reportError.html")
def search(request):
    return render(request,"app/searchAdvance.html")

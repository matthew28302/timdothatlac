from urllib.request import HTTPRedirectHandler
from .models import Account, Item, menuItem
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


from .forms import CreateNewPost

def add_post(request):
    form = CreateNewPost()
    return render(request, "app/post.html", {
        "form": form,
    })
def save_new_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateNewPost(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Luu oke")
        else:
            return HttpResponse("Luu khong thanh cong")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateNewPost()

    return render(request, 'app/post.html', {'form': form})

# Create your views here.
def index(request):
    
    return render(request,'app/index.html',{
        "items": Item.objects.all()
    })



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

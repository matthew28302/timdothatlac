from urllib.request import HTTPRedirectHandler
from .models import Item
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CreateNewPost

@login_required
def add_post(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateNewPost(request.POST)
        # # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('apps:save_form_sucess'))
        else:
            return HttpResponseRedirect(reverse('apps:save_form_fail'))
   
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
    
#save form status
def save_form_sucess(request):
    return render(request, 'app/save_form_sucess.html')

def save_form_fail(request):
    return render(request, 'app/save_form_fail.html')
        
    
def introduce(request):
    return render(request,"app/introduce.html")
def terms(request):
    return render(request,"app/terms.html")
def policy(request):
    return render(request,"app/policy.html")
def donate(request):
    return render(request,"app/payment_page.html")
def donate_complete(request):
    return render(request, "app/donate_complete.html")
def warning(request):
    return render(request,"app/warning.html")
def report(request):
    return render(request,"app/reportError.html")
def search(request):
    return render(request,"app/searchAdvance.html")

def displaynew(request):
    return render(request, "info/news.html", {
        "items": Item.objects.all()
    })


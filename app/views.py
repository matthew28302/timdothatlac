from django.shortcuts import render
from .models import Item, menuItem
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm

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
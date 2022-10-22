from django.shortcuts import render
from .models import Item, menuItem

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
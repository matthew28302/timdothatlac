from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def post(request):
    return render(request, 'app/postNews.html' )

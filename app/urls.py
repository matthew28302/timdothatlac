from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='indexApp'),
    path('post', views.post, name='post'),
    path("<int:item_id>", views.item, name="item"),
    path("register", views.registerPage, name="register")
]


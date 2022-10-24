from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='indexApp'),
    path('post', views.addItem, name='post'),
    path('addItem', views.addItem, name='addItem'),
    path("<int:item_id>", views.item, name="item"),
    path("register", views.registerPage, name="register"),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]


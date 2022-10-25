from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path("resetpwd", views.resetpwd, name="resetpwd"),
    path('postnew', views.postnew, name='postnew') 
]

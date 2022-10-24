from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='indexApp'),
    path('post', views.post, name='post'),
    path("<int:item_id>", views.item, name="item"),
    path("register", views.registerPage, name="register"),
    path('policy/',views.policy,name="policy"),
    path('warning/', views.warning, name="warning"),
    path('donate/', views.donate, name="donate"),
    path('terms/', views.terms, name="terms"),
    path('introduce/', views.introduce, name="introduce"),
    path('report/',views.report,name="reportError"),
    path("search/",views.search, name="searchAdvance"),
]


from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = "apps"
#name space
urlpatterns = [
    path('',views.index,name='indexApp'),
    path('add/', views.add_post, name='postnew'),
    path('save/', views.save_new_post, name='save_new_post'),
    path("<int:item_id>", views.item, name="item"),
    path("register", views.registerPage, name="register"),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('policy/',views.policy,name="policy"),
    path('warning/', views.warning, name="warning"),
    path('donate/', views.donate, name="donate"),
    path('terms/', views.terms, name="terms"),
    path('introduce/', views.introduce, name="introduce"),
    path('report/',views.report,name="reportError"),
    path("search/",views.search, name="searchAdvance"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
from django import forms
from .models import Item
from django.forms import ModelForm
from .models import Item
import re
import datetime



class CreateNewPost(ModelForm):
    postInfo = (
        ('ND','Nhặt được'),
        ('TK','Tìm kiếm'),
    )
    typeItem = (
        ('ID','Ví/Giấy tờ'),
        ('PET','Thú cưng'),
        ('PEOPLE','Người'),
        ('ED','Điện thoại/Tablet/Laptop'),
        ('KEY','Chìa khóa'),
        ('TRANSPORT','Xe máy/Ô tô'),
        ('OTHER','Đồ vật khác'),
    )
   
    postInfo = forms.ChoiceField(help_text='Kiểu tin tức',choices=postInfo,)
    typeItem = forms.ChoiceField(help_text="Loại đồ vật",choices=typeItem,)
    date_time = forms.DateTimeField(initial=datetime.datetime.now())

    class Meta:
        model = Item
        fields = ('title','content','location','postInfo','typeItem','image','email','phone','date_time',)
        

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id':'title_form', }),
            'content': forms.TextInput(attrs={'class': 'form-control', }),
            'location': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            

        }



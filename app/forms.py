from django import forms
from .models import Item

class CreateNewPost(forms.ModelForm):
    # title = models.CharField("Tiêu đề", max_length = 200)
    # postInfo = models.CharField("Kiểu tin tức",max_length=10, choices=_postInfo, blank=True)
    # typeItem = models.CharField("Phân loại đồ", max_length=50, choices=_typeItem,blank=True)
    # adrLost = models.CharField("Địa điểm mất",max_length=200)
    # image = models.ImageField( upload_to='static/app/images/', height_field=None, width_field=None, max_length=None)
    # content = models.CharField("Nội dung", max_length=500)
    # fullname = models.CharField("Họ tên",blank = True, max_length = 100)
    # address = models.CharField("Địa chỉ",blank = True, max_length = 200)
    # phoneNum = models.CharField("Số điện thoại",blank =  True, max_length = 10)
    # email = models.EmailField(("Email"),blank = True, max_length=254)
    class Meta:
        model = Item
        fields = ('title', 'postInfo', 'typeItem', 'adrLost', 'image', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'postInfo': forms.TextInput(attrs={'class': 'form-control', }),
            'typeItem': forms.TextInput(attrs={'class': 'form-control', }),
            'adrLost': forms.TextInput(attrs={'class': 'form-control', }),
            # 'image': forms.ImageField(attrs={'class': 'mx-auto d-block'}),
            'content': forms.Textarea(attrs={'class': 'form-control', }),

        }


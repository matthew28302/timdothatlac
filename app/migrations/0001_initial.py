# Generated by Django 4.1.2 on 2022-12-04 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Tên đăng nhập')),
                ('password', models.CharField(max_length=50, verbose_name='Mật khẩu')),
                ('fullname', models.CharField(blank=True, max_length=100, verbose_name='Họ tên')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='menuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameItem', models.CharField(max_length=50, verbose_name='Tên kiểu đồ')),
                ('amountLost', models.IntegerField(verbose_name='Số lượng mất')),
                ('amountPick', models.IntegerField(verbose_name='Số lượng nhặt được')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100, verbose_name='Người gửi')),
                ('receiver', models.CharField(max_length=50, verbose_name='Người nhận')),
                ('content', models.CharField(max_length=50, verbose_name='Nội dung')),
                ('time', models.DateTimeField(verbose_name='Thời gian')),
                ('status', models.CharField(blank=True, choices=[('W', 'Waiting'), ('S', 'Success'), ('F', 'Failed')], max_length=50, verbose_name='Trạng thái tin nhắn')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Tiêu đề')),
                ('content', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nội dung')),
                ('location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Địa điểm thất lạc đồ')),
                ('postInfo', models.CharField(blank=True, choices=[('ND', 'Nhặt được'), ('TK', 'Tìm kiếm')], max_length=10, null=True, verbose_name='Kiểu tin tức')),
                ('typeItem', models.CharField(blank=True, choices=[('ID', 'Ví/Giấy tờ'), ('PET', 'Thú cưng'), ('PEOPLE', 'Người'), ('ED', 'Điện thoại/Tablet/Laptop'), ('KEY', 'Chìa khóa'), ('TRANSPORT', 'Xe máy/Ô tô'), ('OTHER', 'Đồ vật khác')], max_length=10, null=True, verbose_name='Loại đồ vật')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ảnh đồ vật ( nếu có)')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email liên hệ')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Số điện thoại liên hệ')),
                ('date_time', models.DateTimeField(blank=True, null=True, verbose_name='Thời gian đăng tin')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

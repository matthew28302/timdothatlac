# Generated by Django 4.1.2 on 2022-11-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_item_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='postInfo',
            field=models.CharField(blank=True, choices=[('ND', 'Nhặt được'), ('TK', 'Tìm kiếm')], max_length=10, null=True, verbose_name='Kiểu tin tức'),
        ),
    ]

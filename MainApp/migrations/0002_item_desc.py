# Generated by Django 5.1.3 on 2024-12-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.CharField(default='Описание товара', max_length=100),
        ),
    ]

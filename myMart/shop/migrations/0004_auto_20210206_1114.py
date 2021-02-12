# Generated by Django 3.1.6 on 2021-02-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
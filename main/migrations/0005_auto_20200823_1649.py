# Generated by Django 3.0 on 2020-08-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200822_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pic',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='a product category'),
        ),
    ]
# Generated by Django 3.0 on 2020-08-23 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Color'),
        ),
    ]

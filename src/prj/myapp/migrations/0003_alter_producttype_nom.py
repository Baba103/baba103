# Generated by Django 5.1.5 on 2025-01-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_inpc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='nom',
            field=models.CharField(max_length=100),
        ),
    ]

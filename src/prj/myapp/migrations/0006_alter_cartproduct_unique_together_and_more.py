# Generated by Django 5.1.5 on 2025-01-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_cartproduct_date_from_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartproduct',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='pointofsale',
            name='nom',
            field=models.CharField(max_length=100),
        ),
    ]

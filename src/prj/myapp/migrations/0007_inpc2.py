# Generated by Django 5.1.5 on 2025-02-01 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_cartproduct_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inpc2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.DateField()),
                ('valeur', models.FloatField()),
                ('methode', models.CharField(default='Méthode 2', max_length=255)),
            ],
        ),
    ]

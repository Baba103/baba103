# Generated by Django 5.1.4 on 2025-01-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=252)),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='module',
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=None,
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
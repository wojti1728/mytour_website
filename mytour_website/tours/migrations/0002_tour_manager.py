# Generated by Django 3.1.14 on 2023-10-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='manager',
            field=models.CharField(blank=True, max_length=50, verbose_name='Manager'),
        ),
    ]

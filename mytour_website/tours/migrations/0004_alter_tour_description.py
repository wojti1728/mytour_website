# Generated by Django 4.2.6 on 2023-10-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_remove_tour_day_remove_tour_manager_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
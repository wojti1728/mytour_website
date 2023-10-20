# Generated by Django 4.2.6 on 2023-10-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_remove_sightseeing_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mytouruser',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='thingslist',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tour',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transport',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

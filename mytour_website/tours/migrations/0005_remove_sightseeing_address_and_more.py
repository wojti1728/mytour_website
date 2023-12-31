# Generated by Django 4.2.6 on 2023-10-20 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_tour_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sightseeing',
            name='address',
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='address',
        ),
        migrations.AddField(
            model_name='tour',
            name='accommodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.accommodation'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Accomadation Names'),
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Sightseeing',
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metquery',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

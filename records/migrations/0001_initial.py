# Generated by Django 4.1.5 on 2023-01-09 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('height', models.IntegerField()),
                ('actual_temperature', models.DecimalField(decimal_places=4, max_digits=10)),
                ('virtual_temperature', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pressure', models.DecimalField(decimal_places=4, max_digits=10)),
                ('humidity', models.DecimalField(decimal_places=4, max_digits=10)),
                ('wind_speed', models.DecimalField(decimal_places=4, max_digits=10)),
                ('wind_direction', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RecordForQuery',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('query_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_id', to='query.metquery')),
                ('record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_id', to='records.record')),
            ],
        ),
    ]

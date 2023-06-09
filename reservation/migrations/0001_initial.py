# Generated by Django 2.2.7 on 2023-05-06 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('currentSpeed', models.IntegerField()),
                ('model', models.CharField(max_length=50)),
                ('fuelCapacity', models.IntegerField()),
                ('timeForInspection', models.DateField()),
                ('description', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/Aircrafts_img/')),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10)),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Aircraft')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

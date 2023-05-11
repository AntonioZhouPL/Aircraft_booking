from django.db import models

from accounts.models import User
#from accounts.models import User


# Create your models here.
class Aircraft(models.Model):
    id = models.BigAutoField(primary_key=True)
    currentSpeed = models.IntegerField()
    model = models.CharField(max_length = 50)
    fuelCapacity = models.IntegerField()
    timeForInspection = models.DateField()
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='static/Aircrafts_img/', blank=True, null=True)
    availability = models.BooleanField()
    country = models.CharField(max_length=100,default='Unknown')


    #users = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')



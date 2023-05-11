from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_user = models.BooleanField(default=False)
    is_engineer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        # abstract = True
        pass

    def __str__(self):
        return self.first_name + self.last_name


class Employee(models.Model):
    user_field = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    certificate = models.ImageField(upload_to='media/certificates/', blank=True, null=True)
    salary = models.IntegerField()


class Admin(models.Model):
    user_field = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    admin_field = models.CharField(max_length=50)


class Engineer(models.Model):
    user_field = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50)

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guest_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    reason_for_visit = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    last_visit = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

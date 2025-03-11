from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    email = models.EmailField()
    reason_for_visit = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    last_visit = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Enhancement(models.Model):
#     enhancement_id = models.AutoField(primary_key=True)
#     enhancement_name = models.CharField(max_length=50)
#     enhancement_description = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images/')
#     quanity = models.IntegerField()
#     enhancement_price = models.DecimalField(max_digits=6, decimal_places=2)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     reservation = models.ForeignKey(
#         Reservation,
#         on_delete=models.CASCADE,
#         related_name='enhancements')

#     def __str__(self):
#         return self.enhancement_name


# class Payment(models.Model):
#     payment_id = models.AutoField(primary_key=True)
#     payment_date = models.DateTimeField()
#     payment_amount = models.DecimalField(max_digits=6, decimal_places=2)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     reservation = models.ForeignKey(
#         Reservation,
#         on_delete=models.CASCADE,
#         related_name='payments')

#     def __str__(self):
#         return f"{self.payment_date} {self.payment_amount}"


# class Review(models.Model):
#     review_id = models.AutoField(primary_key=True)
#     review_date = models.DateTimeField()
#     review_text = models.CharField(max_length=200)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     guest = models.ForeignKey(
#         Guest, on_delete=models.CASCADE, related_name='reviews')
#     Reservation = models.ForeignKey(
#         Reservation,
#         on_delete=models.CASCADE,
#         related_name='reviews')

#     def __str__(self):
#         return self.review_text

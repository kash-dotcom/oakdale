from django.db import models
from guest.models import Guest
from experience.models import Experience

# Create your models here.


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    reservation_date = models.DateTimeField()
    number_of_guests = models.IntegerField()
    reservation_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name='reservations')
    guest = models.ForeignKey(
        Guest,
        on_delete=models.CASCADE,
        related_name='guest_reservations')

    def __str__(self):
        return f"{self.reservation_date.strftime('%Y-%m-%d')} - {self.number_of_guests} guests"

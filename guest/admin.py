from django.contrib import admin
from .models import (
    Guest, Reservation, Experience, Payment, Review, Enhancement
)

# Register your models here.
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Experience)
admin.site.register(Enhancement)
admin.site.register(Review)

from django.contrib import admin
from .models import (
    Guest, Reservation, Experience, Payment, Review, Enhancements, ValuedGuest
)

# Register your models here.
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Experience)
admin.site.register(Enhancements)
admin.site.register(Review)
admin.site.register(ValuedGuest)

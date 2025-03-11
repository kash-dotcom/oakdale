from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    experience_name = models.CharField(max_length=50)
    experience_description = models.CharField(max_length=200)
    experience_image = CloudinaryField('image', default='placeholder')
    experience_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.experience_name
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import ExperienceList

# Create your views here.

urlpatterns = [
    path('', ExperienceList.as_view(), name='experience_list'),
]

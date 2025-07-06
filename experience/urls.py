from django.urls import path
from .views import ExperienceList

# Create your views here.

urlpatterns = [
    path('', ExperienceList.as_view(), name='experience_list'),
]

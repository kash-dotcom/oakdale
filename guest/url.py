from . import views
from django.urls import path

# Create your views here.

urlpatterns = [
    path('', ExperienceList.as_view(), name='experience_list'),
]

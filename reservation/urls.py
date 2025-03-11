from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('add/', views.add_reservation, name='add_reservation'),
    path('delete', views.delete_reservation, name='delete_reservation'),
    path('update', views.update_reservation, name='update_reservation'),
]

from django.urls import path
from . import views
from .views import ReservationListView

urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation'),
    # path('get_experience_price/<int:experience_id>/', views.get_experience_price, name='get_experience_price'),
    path('add/', views.add_reservation, name='add_reservation'),
]
    # path('delete/', views.delete_reservation, name='delete_reservation'),
    # path('update/', views.update_reservation, name='update_reservation'),

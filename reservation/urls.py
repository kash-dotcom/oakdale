from django.urls import path
from . import views
from .views import ReservationListView

urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation'),
    # path('get_experience_price/<int:experience_id>/',
    #      views.get_experience_price, name='get_experience_price'),
    path('add/', views.add_reservation, name='add_reservation'),
    path('confirmation/<int:reservation_id>', views.confirmation,
         name='confirmation'),
    path('past_reservations/', views.past_reservations,
         name='past_reservations'),
    path('delete/', views.delete_reservation, name='delete_reservation'),
    path('change/<int:reservation_id>', views.change_reservation,
         name='change_reservation'),
    path('reservation/change/<int:reservation_id>/', views.change_reservation,
         name='change_reservation'),
]

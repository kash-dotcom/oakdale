from django.shortcuts import render

# Create your views here.


def reservation(request):
    return render(request, 'reservation.html', {})


def add_reservation(request):
    return render(request, 'add_reservation.html', {})


def delete_reservation(request):
    return render(request, 'delete_reservation.html', {})


def update_reservation(request):
    return render(request, 'update_reservation.html', {})

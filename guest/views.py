from django.shortcuts import render
from django.views import generic
from .models import Experience


# Create your views here.

class ExperienceList(generic.ListView):
    model = Experience


# def index(request):
#     return render(request, "guest/index.html")


# class client:
#     template_name = "guest/index.html"
#     model = Guest

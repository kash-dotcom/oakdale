from django.shortcuts import render
from django.views import generic
from .models import Experience


# Create your views here.

class ExperienceList(generic.ListView):
    model = Experience
    queryset = Experience.objects.filter(publish=True)
    template_name = "home.html"


def home(request):
    experience_list = Experience.objects.filter(publish=True)
    return render(request, "guest/home.html", {
        'experience_list': experience_list})


# class client:
#     template_name = "guest/index.html"
#     model = Guest

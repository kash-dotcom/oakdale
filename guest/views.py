from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "guest/index.html")


class client:
    template_name = "guest/index.html"

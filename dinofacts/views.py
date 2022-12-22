from django.shortcuts import render
from rest_framework import viewsets
from .models import Dino

# Create your views here.
from datetime import datetime
from django.shortcuts import render

def show_dino(request, name):
    data = {
        "dinosaurs": [
            "Tyrannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops",
        ],
        "now": datetime.now(),
        "numbers": [1,2,3,4,5]
    }

    return render(request, name + ".html", data)

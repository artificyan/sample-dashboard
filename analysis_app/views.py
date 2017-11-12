from analysis_app.models import Trips
from django.shortcuts import render
import pandas as pd

def home(request):
    test_trips = Trips.objects.all()
    return render(request, 'analysis_app/home.html', {'test_trips': test_trips})

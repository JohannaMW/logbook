from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from logbook.forms import TravellerForm, JourneyForm
from logbook.models import Journey
import json

def home(request):
    return render(request, 'home.html', {})

def my_journeys(request):
    journeys = Journey.objects.filter(user=request.user)
    return render(request, 'my_journeys.html', {'journeys':journeys})

def profile(request):
    journeys = Journey.objects.filter(user=request.user)
    return render(request, 'profile.html', {'journeys':journeys})

def add_journey(request):
    if request.method == 'POST':
        form = JourneyForm(request.POST, request.FILES)
        if form.is_valid():
             if form.save():
                return redirect("profile")
    else:
        form = JourneyForm()
    data = {"form": form}
    return render(request, "add_journey.html", data)

# Registration
def register(request):
    if request.method == 'POST':
        form = TravellerForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("profile")
    else:
        form = TravellerForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

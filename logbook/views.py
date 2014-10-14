from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from logbook.forms import TravellerForm, JourneyForm
from logbook.models import Journey
import json

def home(request):
    return render(request, 'home.html', {})

@login_required
def my_journeys(request):
    # should be able to just do request.user.journeys do to the related_name you have set up
    journeys = Journey.objects.filter(user=request.user)
    # Should this URL just be in a setting? seems redundant to include this in a lot of the views
    # Would be annoying to replace if this changes
    url = "https://s3-us-west-2.amazonaws.com/myfirstbucket1503/"
    return render(request, 'my_journeys.html', {'journeys':journeys, 'url':url})

@login_required
def map(request):
    # should be able to just do request.user.journeys do to the related_name you have set up
    journeys = Journey.objects.filter(user=request.user)
    url = "https://s3-us-west-2.amazonaws.com/myfirstbucket1503/"
    return render(request, 'map.html', {'journeys':journeys, 'url':url})

@login_required
def add_journey(request):
    if request.method == 'POST':
        form = JourneyForm(request.POST, request.FILES)
        if form.is_valid():
            # Adding commit = False will make it so it does not try to save it
            # This will let you make the user field required again on your Journey model
            new_journey = form.save(commit=False)
            new_journey.user = request.user
            new_journey.save()
            return redirect("/map/")
    else:
        form = JourneyForm()
    data = {"form": form}
    return render(request, "add_journey.html", data)

@login_required
def edit_journey(request, journey_id):
    journey = Journey.objects.get(id=journey_id)
    if request.method == 'POST':
        form = JourneyForm(request.POST, request.FILES, instance=journey)
        if form.is_valid():
             if form.save():
                return redirect("/journeys/{}".format(journey_id))
    else:
        form = JourneyForm(instance=journey)
    data = {"form": form}
    return render(request, "edit_journey.html", data)

@login_required
def remove_journey(request, journey_id):
    journey = Journey.objects.get(id=journey_id)
    journey.delete()
    return redirect("/journeys")

@login_required
def view_journey(request, journey_id):
    # What happens if someone inputs a bad journey_id?
    journey = Journey.objects.get(id=journey_id)
    url = "https://s3-us-west-2.amazonaws.com/myfirstbucket1503/"
    return render(request, 'view_journey.html', {'journey':journey, 'url':url})

# Registration
def register(request):
    if request.method == 'POST':
        form = TravellerForm(request.POST)
        if form.is_valid():
            # should use form.cleaned_data["username"]
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect("map")
    else:
        form = TravellerForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

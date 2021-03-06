import json
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.generic import ListView
from django.http import JsonResponse,HttpResponse
from .models import TestData,User
from .Algorithms.BallisticThrow import BallisticThrow
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(request, "TestResults/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "TestResults/login.html")


def logout_view(request):
    logout(request)
    return redirect(reverse("login_view"))


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = f"{first_name}_{last_name}"
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "TestResults/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username, email, password, first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError:
            return render(request, "TestResults/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect(reverse("index"))
    else:
        return render(request, "TestResults/register.html")


def index(request):
    if request.user.is_authenticated:
        return render(request, "TestResults/throw_sim.html")
    return redirect(reverse("login"))


class ResultsView(ListView):
    model = TestData


def submit_sim(request):
    if request.method == "POST":
        data = json.loads(request.body)
        height = float(data["height"])
        velocity = float(data["velocity"])
        angle = float(data["angle"])

        problem = BallisticThrow(0, height, velocity, angle)
        results = problem.get_data()
        return JsonResponse(results)

    return JsonResponse({"API_endpoint": "BallisticThrow"})

@csrf_exempt # Temp! remove after validation
def record_sim(request):
    if request.method == "POST":
        # data = json.loads(request.body)

        # data_entry = TestData()
        return HttpResponse(status=200)
    return HttpResponse(status=500)


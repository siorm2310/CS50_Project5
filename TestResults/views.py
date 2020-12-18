from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"TestResults/throw_sim.html")
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("api/sumbit", views.simulation_api, name="simulation_api"),
    path("results", views.ResultsView.as_view(), name="results"),
]

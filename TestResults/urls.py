from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("api/submit", views.submit_sim, name="submit_sim"),
    path("api/record", views.record_sim, name="record_sim"),
    path("results", views.ResultsView.as_view(), name="results"),
]

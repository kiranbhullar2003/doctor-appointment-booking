from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage),
    path('register', views.registerPage),
    path("dashboard", views.dashboard),
    path("dashboardpatient", views.dashboardpatient),
    path("appointments", views.appointments),
    path("appointmentdetail", views.Appointmentdetail),
    path("api/register", views.register),
    path("api/login", views.login_view),
    path("form", views.form),
]

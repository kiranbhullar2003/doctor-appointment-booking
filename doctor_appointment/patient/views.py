from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

def landingPage (request):
    return render(request, "landing_page.html")
 
def registerPage (request):
    return render(request, "registerPage.html")
 
def dashboard (request):
    context = {
        "doctors" : [], "appointments" : []
    }

    all_doctors = Doctor.objects.all()
    for doctor in all_doctors:
        temp = {
            "name" : doctor.userId.username,
        }
        context["doctors"].append(temp)
    all_appointments = Appointment.objects.all() 
    for appointment in all_appointments:
        temp = {
            "doctor_name" : appointment.docId.userId.username,
            "date" : appointment.date,
            "reason": appointment.reason,
            "patient_name": appointment.name,
            "patient_age": appointment.age,
            "patient_gender": appointment.gender,
            "patient_email": appointment.email,
            "patient_phone": appointment.phone_number,
        }
        context["appointments"].append(temp)   
    return render(request, "dashboard.html", context)

def dashboardpatient(request):
    context = {
        "doctors": list(Doctor.objects.all()),
        "appointments" : Appointment.objects.filter(userId__id=request.user.id)
    }
    print(context)
    return render(request, "dashboardpatient.html", context)

def form(request):
    return render(request, "form.html")

def appointments(request):
    context = {
        "appointments" : []
    }

    all_appointments = Appointment.objects.all()

    for appointment in all_appointments:
        temp = {
            "doctor_name" : appointment.docId.userId.username,
            "date" : appointment.date,
            "reason": appointment.reason,
            "patient_name": appointment.name,
            "patient_age": appointment.age,
            "patient_gender": appointment.gender,
            "patient_email": appointment.email,
            "patient_phone": appointment.phone_number,
        }
        context["appointments"].append(temp)

    return render(request, "appointments.html", context)

def Appointmentdetail(request):
    return render(request, "appointment_detail.html")


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('register_username')
            email = data.get('register_email')
            password = data.get('register_password')
            phone_number = data.get('register_phone_number')
            print(data)

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON.'})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        username = data.get('login_username')
        password = data.get('login_password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
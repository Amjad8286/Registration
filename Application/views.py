from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import incidents


# Create your views here.
def user_login(request):
    if request.method == 'POST':

        username1 = request.POST.get('username1')
        password1 = request.POST.get('password1')
        user = authenticate(username=username1, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("register")

    return render(request, 'application/authentication-login1.html')


def report(request):
    if request.method == 'POST':
        location = request.POST.get('location', '')
        incident_department = request.POST.get('incident_department', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        incident_location = request.POST.get('incident_location', '')
        initial_severty = request.POST.get('initial_severty', '')
        suspected_Cause = request.POST.get('suspected_Cause', '')
        immediate_action = request.POST.get('immediate_action', '')
        Enviromental_Incident = request.POST.get('Enviromental_Incident', '')
        injuryillness = request.POST.get('injuryillness', '')
        Property_damage = request.POST.get('Property_damage', '')
        vehicle = request.POST.get('vehicle', '')

        person = incidents(location=location, incident_department=incident_department,
                           date=date, time=time, incident_location=incident_location,
                           initial_severty=initial_severty, suspected_Cause=suspected_Cause,
                           immediate_action=immediate_action, Enviromental_Incident=Enviromental_Incident,
                           injuryillness=injuryillness, Property_damage=Property_damage, vehicle=vehicle, )

        person.save()
        return redirect('submit')
    else:

        return render(request, 'application/report-form.html')


def index(request):
    return render(request, 'application/index.html')


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        myuser = User.objects.create_user(username, email, password)

        myuser.save()
        myuser.FIRST_NAME = username
        messages.success(request, " Your account has been successfully created")
        return redirect('user_login')

    else:
        return render(request, "application/authentication-register1.html")


def submit(request):
    return render(request, 'application/submit-incident.html')


def handle_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('user_login')

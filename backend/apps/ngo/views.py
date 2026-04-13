from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


# HOME PAGE
def home(request):
    from apps.ngo.models import NGO

    ngo_count = NGO.objects.count()
    total_donations = 0
    event_count = 0

    return render(request, 'home.html', {
        'ngo_count': ngo_count,
        'total_donations': total_donations,
        'event_count': event_count
    })


# REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)

        return redirect('/login/')

    return render(request, 'register.html')


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('/')


# DASHBOARD
@login_required(login_url='/login/')
def dashboard_view(request):
    from apps.ngo.models import NGO

    ngos = NGO.objects.all()

    return render(request, 'dashboard.html', {
        'ngos': ngos
    })
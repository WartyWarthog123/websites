from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Change to your desired redirect page
    else:
        form = AuthenticationForm()
    return render(request, 'periodicTable/login.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# User Registration
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or home page
    else:
        form = UserCreationForm()
    return render(request, 'periodicTable/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'periodicTable/dashboard.html')

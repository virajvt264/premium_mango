from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('login')
            
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@csrf_protect
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout successful!')
        return redirect('login')  # Redirect to login page after logout
    return redirect('dashboard')  # If GET request, redirect back to dashboard
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm
def home(request):
    return render(request, 'index.html')

def service_engine_repair(request):
    return render(request, 'service_engine_repair.html')

def service_oil_change(request):
    return render(request, 'service_oil_change.html')

def service_suspension_repair(request):
    return render(request, 'service_suspension_repair.html')

def service_body_repair(request):
    return render(request, 'service_body_repair.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Предполагается, что у вас есть URL для входа
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
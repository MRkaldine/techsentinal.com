from django.shortcuts import render, redirect
from .forms import AppointmentForm


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/contact-form.html', {'form': form})


def confirmation(request):
    return render(request, 'appointments/confirmation.html')


def contact_view(request):
    return render(request, 'appointments/contact-form.html')


def home(request):
    return render(request, 'appointments/beauty.html')  # homepage


def services_view(request):
    return render(request, 'appointments/services.html')


def about_view(request):
    return render(request, 'appointments/about.html')

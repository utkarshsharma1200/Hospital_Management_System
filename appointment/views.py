from django.shortcuts import render, redirect
from .models import DoctorProfile

# 1. Dashboard jahan doctors ki list dikhti hai
def book_appointment(request):
    if request.method == "POST":
        # Button dabne par seedha payment par bhej raha hai
        return redirect('/appointment/payment/1/')
    
    doctors = DoctorProfile.objects.all()
    return render(request, 'appointment/book.html', {'doctors': doctors})

# 2. Payment Page jahan fees dikhti hai
def payment_page(request, appointment_id):
    return render(request, 'appointment/payment.html', {'id': appointment_id})

# 3. Success Page jahan Receipt aur Details dikhti hain
def success_view(request):
    context = {
        'doc_name': 'Dr. Sharma (Senior Surgeon)',
        'time': '11:45 AM',
        'date': '15 March 2026',
        'trans_id': 'WC99824X'
    }
    return render(request, 'appointment/success.html', context)
def home_page(request):
    return render(request, 'appointment/home.html')
from django.db import models

class DoctorProfile(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class AvailabilitySlot(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def _str_(self):
        return f"{self.doctor.name} - {self.date}"
class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=15, default="0000000000")
    date = models.DateField()
    amount = models.IntegerField(default=500)  # Presentation ke liye fix fees
    is_paid = models.BooleanField(default=False) # Payment status check karne ke liye

    def _str_(self):
        return f"{self.patient_name} - {self.doctor.name}"
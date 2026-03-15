from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('payment/<int:appointment_id>/', views.payment_page, name='payment_page'),
    path('success/', views.success_view, name='success_page'),
    path('', views.home_page, name='home')
    
]
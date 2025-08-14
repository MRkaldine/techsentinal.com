from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='beauty'),  # 👈 Add this
    path('contact/', views.book_appointment, name='contact'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('services/', views.services_view, name='services'),
    path('about/', views.about_view, name='about'),
]

from django.contrib import admin
from appointments.models import Appointment

# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'date')
    search_fields = ('name', 'email', 'service')


admin.site.register(Appointment, AppointmentAdmin)

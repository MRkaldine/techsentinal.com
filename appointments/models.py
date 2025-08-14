from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        formatted_date = self.date.strftime('%Y-%m-%d %H:%M')
        return f"{self.name} - {self.service} on {formatted_date}"

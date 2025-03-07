from django.contrib.auth.models import User
from django.db import models

class Accommodation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure ForeignKey to User
    hostel_required = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    def __str__(self):
        return f"Accommodation - {self.user.username}, Hostel: {self.hostel_required}"

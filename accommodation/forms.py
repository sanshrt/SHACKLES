# forms.py

from django import forms
from .models import Accommodation

class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = [ 'gender', 'hostel_required']  # Include fields in the form

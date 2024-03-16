from django import forms
from .models import ReportModel

class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = ['image', 'title', 'description', 'latitude', 'longitude', 'location_name']

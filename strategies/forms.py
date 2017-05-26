from django import forms
from .models import Strategy, Steps

class StratForm(forms.ModelForm):

    class Meta:
        model = Strategy
        fields = ["name"]

class StepForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = ["user", "command", "image"]
        labels = {
            "image": "Image"
        }

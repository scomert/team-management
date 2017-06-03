from django import forms
from .models import Strategy, Steps


class StratForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = ["name"]


class StepForm(forms.ModelForm):

    priority = forms.ChoiceField()

    class Meta:
        model = Steps
        fields = ["user", "command", "priority", "image"]
        labels = {
            "image": "Image"
        }

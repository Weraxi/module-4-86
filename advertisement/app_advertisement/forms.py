from django.forms import models
from django import forms
from django.core.exceptions import ValidationError
from .models import Advertisement

class AdvertisementForm(models.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["title", "description", "price", "auction", "image"]
        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control form-control-lg",
            }),

            "price": forms.NumberInput(attrs={
                "class": "form-control form-control-lg",
            }),

            "auction": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),

            "image": forms.FileInput(attrs={
                "class": "form-control form-control-lg",
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title and title.startswith("?"):
            raise ValidationError("Ошибка")
        return title
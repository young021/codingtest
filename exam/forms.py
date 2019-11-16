from .models import Seed
from django import forms

class SeedForm(forms.ModelForm):
    class Meta:
        model=Seed        # 이거 맞나????
        fields=['name','age',]

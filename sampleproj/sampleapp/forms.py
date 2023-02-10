from django import forms
from . import models

class MyModelForm(forms.ModelForm):
    class Meta:
        model = models.MyModel
        fields = [
            'col1',
        ]
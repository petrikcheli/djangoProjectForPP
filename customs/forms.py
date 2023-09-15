from django import forms
from .models import customs

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = customs
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city', 'color', 'size', 'material', 'properties']

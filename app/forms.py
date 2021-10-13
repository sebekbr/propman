from django import forms
from .models import HousingAssociation


class HousingAssociationForm(forms.ModelForm):
    class Meta:
        model = HousingAssociation
        fields = ('name', 'address', 'postalcode', 'city', 'phone', 'email', 'comments')


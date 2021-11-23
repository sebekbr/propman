from django import forms
from app.models import *


# Spółdzielnie/Wspólnoty mieszkaniowe - przekazywanie pól do wyświetlania
class HousingAssociationForm(forms.ModelForm):
    class Meta:
        model = HousingAssociation
        fields = ('name', 'address', 'postalcode', 'city', 'phone', 'email', 'comments')


# Najemcy
class TenantsForm(forms.ModelForm):
    class Meta:
        model = Tenants
        fields = ('name', 'surname', 'address', 'postalcode', 'city', 'phone', 'email', 'comments')


# Właściciele
class LandlordsForm(forms.ModelForm):
    class Meta:
        model = Landlords
        fields = ('name', 'surname', 'phone', 'email')


# Nieruchomości
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('name', 'address', 'postalcode', 'city', 'house_association', 'kw_number')


# Umowy najmu
class LeaseAgreementForm(forms.ModelForm):
    class Meta:
        model = LeaseAgreement
        fields = ('start', 'end', 'value', 'comments', 'type')


# Dostawcy rachunków
class BillVendorsForm(forms.ModelForm):
    class Meta:
        model = BillVendors
        fields = ('name', 'address', 'postalcode', 'city', 'phone', 'email')


# Rachunki i umowy
class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ('name', 'agreement_number', 'start', 'duration', 'end')


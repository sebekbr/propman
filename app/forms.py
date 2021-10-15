from django import forms
from .models import HousingAssociation
from .models import Tenants
from .models import Landlords
from .models import Property
from .models import LeaseAgreement
from .models import BillVendors
from .models import Bills


# # Użytkownicy systemu
# class UsersForm(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = ['login', 'password', 'name', 'surname', 'type']


# Spółdzielnie/Wspólnoty mieszkaniowe
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
        fields = ('name', 'address', 'postalcode', 'city', 'kw_number')


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
        fields = ('name', 'agreement_number', 'start', 'duration', 'end', 'phone', 'email')
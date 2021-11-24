from django import forms
from app.models import *
from django.utils.translation import ugettext_lazy as _


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
        fields = ('start', 'end', 'value', 'comments', 'type', 'property', 'landlords', 'tenants')
        labels = {
            'start': _('Data początkowa'),
            'end': _('Data końcowa'),
            'value': _('Czynsz'),
            'comments': _('Uwagi'),
            'type': _('Typ'),
            'property': _('Nieruchomość'),
            'landlords': _('Właściciel'),
            'tenants': _('Najemca')
        }
        help_texts = {
            'start': _('W formacie RRRR-MM-DD'),
            'end': _('W formacie RRRR-MM-DD'),
            'value': _('Wpisz umówioną kwotę czynszu')
        }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


# Dostawcy rachunków
class BillVendorsForm(forms.ModelForm):
    class Meta:
        model = BillVendors
        fields = ('name', 'address', 'postalcode', 'city', 'phone', 'email')
        labels = {
            'name': _('Nazwa'),
            'address': _('Adres'),
            'postalcode': _('Kod pocztowy'),
            'city': _('Miasto'),
            'phone': _('Numer telefonu'),
            'email': _('E-mail')
        }
        help_texts = {
            'start': _('W formacie RRRR-MM-DD'),
            'end': _('W formacie RRRR-MM-DD'),
            'value': _('Wpisz umówioną kwotę czynszu')
        }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


# Rachunki i umowy
class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ('name', 'agreement_number', 'bill_vendor', 'property', 'start', 'duration', 'end')
        labels = {
            'start': _('Data początkowa'),
            'end': _('Data końcowa'),
            'agreement_number': _('Numer mowy'),
            'name': _('Nazwa'),
            'bill_vendor': _('Dostawca'),
            'property': _('Nieruchomość'),
            'duration': _('Czas trwania')
        }
        help_texts = {
            'start': _('W formacie RRRR-MM-DD'),
            'end': _('W formacie RRRR-MM-DD'),
        }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


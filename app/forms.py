from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from app.models import *
from django.utils.translation import ugettext_lazy as _


# Spółdzielnie/Wspólnoty mieszkaniowe - przekazywanie pól do wyświetlania
class HousingAssociationForm(forms.ModelForm):
    class Meta:
        model = HousingAssociation
        fields = ['name', 'address', 'postalcode', 'city', 'phone', 'email', 'type', 'comments']
        labels = {
            'name': _('Nazwa'),
            'address': _('Adres'),
            'postalcode': _('Kod pocztowy'),
            'city': _('Miasto'),
            'phone': _('Telefon'),
            'email': _('E-mail'),
            'type': _('Rodzaj'),
            'comments': _('Uwagi')
        }
        # help_texts = {
        #     'start': _('W formacie RRRR-MM-DD'),
        #     'end': _('W formacie RRRR-MM-DD'),
        #     'value': _('Wpisz umówioną kwotę czynszu')
        # }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


# Najemcy
class TenantsForm(forms.ModelForm):
    class Meta:
        model = Tenants
        fields = ['name', 'surname', 'address', 'postalcode', 'city', 'phone', 'email', 'comments']
        labels = {
            'name': _('Imię'),
            'surname': _('Nazwisko'),
            'address': _('Adres'),
            'postalcode': _('Kod pocztowy'),
            'city': _('Miasto'),
            'phone': _('Telefon'),
            'email': _('E-mail'),
            'comments': _('Uwagi')
        }
        # help_texts = {
        #     'start': _('W formacie RRRR-MM-DD'),
        #     'end': _('W formacie RRRR-MM-DD'),
        #     'value': _('Wpisz umówioną kwotę czynszu')
        # }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


# Właściciele
class LandlordsForm(forms.ModelForm):
    class Meta:
        model = Landlords
        fields = ['name', 'surname', 'phone', 'email']
        labels = {
            'name': _('Imię'),
            'surname': _('Nazwisko'),
            'phone': _('Telefon'),
            'email': _('E-mail')
        }
        # help_texts = {
        #     'start': _('W formacie RRRR-MM-DD'),
        #     'end': _('W formacie RRRR-MM-DD'),
        #     'value': _('Wpisz umówioną kwotę czynszu')
        # }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


# Nieruchomości
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'postalcode', 'city', 'house_association', 'kw_number']
        labels = {
            'name': _('Nazwa'),
            'address': _('Adres'),
            'postalcode': _('Kod pocztowy'),
            'city': _('Miasto'),
            'house_association': _('Spółdzielnia/wspólnota'),
            'kw_number': _('Numer księgi wieczystej')
        }
        # help_texts = {
        #     'start': _('W formacie RRRR-MM-DD'),
        #     'end': _('W formacie RRRR-MM-DD'),
        #     'value': _('Wpisz umówioną kwotę czynszu')
        # }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


# Umowy najmu
class LeaseAgreementForm(forms.ModelForm):
    class Meta:
        model = LeaseAgreement
        fields = ['la_number', 'start', 'end', 'value', 'payment_day',
                  'comments', 'type', 'property', 'landlords', 'tenants']
        labels = {
            'la_number': _('Numer umowy'),
            'start': _('Data początkowa'),
            'end': _('Data końcowa'),
            'value': _('Czynsz'),
            'payment_day': _('Data płatności'),
            'comments': _('Uwagi'),
            'type': _('Typ'),
            'property': _('Nieruchomość'),
            'landlords': _('Właściciel'),
            'tenants': _('Najemca')
        }
        widgets = {
            'start': DatePickerInput(
                options={
                    "format": "DD.MM.YYYY", # moment date-time format
                    "showClose": False,
                    "showClear": False,
                    "showTodayButton": False,
                    "locale": "PL",
                }
            ),  # default date-format %m/%d/%Y will be used
            'end': DatePickerInput(
                options={
                    "format": "DD.MM.YYYY", # moment date-time format
                    "showClose": False,
                    "showClear": False,
                    "showTodayButton": False,
                    "locale": "PL",
                }),  # specify date-frmat
        }
        help_texts = {
            'start': _('W formacie RRRR-MM-DD'),
            'end': _('W formacie RRRR-MM-DD'),
            'value': _('Wpisz umówioną kwotę czynszu')
        }

    def clean(self):
        start_date = self.cleaned_data['start']
        end_date = self.cleaned_data['end']

        if end_date <= start_date:
            raise forms.ValidationError({'end': 'Data końcowa nie może być wczesniejsza niż początkowa.'})


# Dostawcy rachunków
class BillVendorsForm(forms.ModelForm):
    class Meta:
        model = BillVendors
        fields = ['name', 'address', 'postalcode', 'city', 'phone', 'email']
        labels = {
            'name': _('Nazwa'),
            'address': _('Adres'),
            'postalcode': _('Kod pocztowy'),
            'city': _('Miasto'),
            'phone': _('Numer telefonu'),
            'email': _('E-mail')
        }
        # help_texts = {
        #     'start': _('W formacie RRRR-MM-DD'),
        #     'end': _('W formacie RRRR-MM-DD'),
        #     'value': _('Wpisz umówioną kwotę czynszu')
        # }
        # error_messages = {
        #     'type': {
        #         'max_length': _("Zbyt duża ilość znaków."),
        #     },
        # }


# Rachunki i umowy
class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ['name', 'agreement_number', 'bill_vendor', 'property', 'start', 'duration', 'end']
        labels = {
            'name': _('Nazwa'),
            'agreement_number': _('Numer umowy'),
            'bill_vendor': _('Dostawca'),
            'property': _('Nieruchomość'),
            'start': _('Data początkowa'),
            'duration': _('Czas trwania'),
            'end': _('Data końcowa'),
        }
        widgets = {
            'start': DatePickerInput(
                options={
                    "format": "DD.MM.YYYY",  # moment date-time format
                    "showClose": False,
                    "showClear": False,
                    "showTodayButton": False,
                    "locale": "PL",
                }
            ),
            'end': DatePickerInput(
                options={
                    "format": "DD.MM.YYYY",  # moment date-time format
                    "showClose": False,
                    "showClear": False,
                    "showTodayButton": False,
                    "locale": "PL",
                }),
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

    def clean(self):
        start_date = self.cleaned_data['start']
        end_date = self.cleaned_data['end']

        if end_date <= start_date:
            raise forms.ValidationError({'end': 'Data końcowa nie może być wcześniejsza niż początkowa.'})


from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from .forms import *


def index(request):
    return render(request, 'registration/home.html')


#############################
# Housing Association methods
# class HousingAssociationView(View):
#     def get(self, request, *args, **kwargs):
#         form = self.HousingAssociation(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')
#
#         return render(request, self.template_name, {'form': form})
#
#     def list(self, request):
#         form = HousingAssociation.objects.all()
#         return render(request, 'registration/ha/ha_list.html', {'ha_all': form})
#
#     def detail(self, request, pk):
#         self.form = get_object_or_404(HousingAssociation, pk=pk)
#         return render(request, 'registration/ha/ha_detail.html', {'ha_detail': self.form})
#
#     # Zapisywanie formularza
#     def new(self, request):
#         if request.method == "POST":
#             form = HousingAssociationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return render(request, 'registration/ha/success.html')  # Render strony po pomyślnym utworzeniu
#         else:
#             form = HousingAssociationForm()
#             return render(request, 'registration/ha/ha_new.html', {'housingassociation_new': form})
#
#     # Edycja wpisu
#     def edit(self, request, pk):
#         detail = get_object_or_404(HousingAssociation, pk=pk)
#         if request.method == "POST":
#             form = HousingAssociationForm(request.POST, instance=detail)
#             if form.is_valid():
#                 form.save()
#                 return render(request, 'registration/ha/success.html')  # Render strony po pomyślnym zapisaniu
#         else:
#             form = HousingAssociationForm(instance=detail)
#         return render(request, 'registration/ha/ha_edit.html', {'ha_edit': form})
#
#     def success(self, request):
#         return render(request, 'registration/ha/success.html', {'ha_success': self.success})

def ha_list(request):
    form = HousingAssociation.objects.all()
    return render(request, 'registration/ha/ha_list.html', {'ha_all': form})


def housingassociation_detail(request, pk):
    form = get_object_or_404(HousingAssociation, pk=pk)
    return render(request, 'registration/ha/ha_detail.html', {'ha_detail': form})


# Zapisywanie formularza
def housingassociation_form_new(request):
    if request.method == "POST":
        form = HousingAssociationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/ha/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = HousingAssociationForm()
        return render(request, 'registration/ha/ha_new.html', {'housingassociation_new': form})


# Edycja wpisu
def housingassociation_form_edit(request, pk):
    detail = get_object_or_404(HousingAssociation, pk=pk)
    if request.method == "POST":
        form = HousingAssociationForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/ha/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = HousingAssociationForm(instance=detail)
    return render(request, 'registration/ha/ha_edit.html', {'ha_edit': form})


def housingassociation_success(request):
    return render(request, 'registration/ha/success.html', {'ha_success': housingassociation_success})


#################
# Tenants methods
def tenant_list(request):
    form = Tenants.objects.all()
    return render(request, 'registration/tenants/tenant_list.html', {'tenant_all': form})


def tenant_detail(request, pk):
    form = get_object_or_404(Tenants, pk=pk)
    return render(request, 'registration/tenants/tenant_detail.html', {'tenant_detail': form})


# Zapisywanie formularza
def tenant_form_new(request):
    if request.method == "POST":
        form = TenantsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/tenants/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = TenantsForm()
        return render(request, 'registration/tenants/tenant_new.html', {'tenant_new': form})


# Edycja wpisu
def tenant_form_edit(request, pk):
    detail = get_object_or_404(Tenants, pk=pk)
    if request.method == "POST":
        form = TenantsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/tenants/tenant_edit_success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = TenantsForm(instance=detail)
    return render(request, 'registration/tenants/tenant_edit.html', {'tenant_edit': form})


def tenant_success(request):
    return render(request, 'registration/tenants/success.html', {'tenant_success': tenant_success})


##################
# Landlord methods
def landlord_list(request):
    form = Landlords.objects.all()
    return render(request, 'registration/landlord/landlord_list.html', {'landlord_all': form})


def landlord_detail(request, pk):
    form = get_object_or_404(Landlords, pk=pk)
    return render(request, 'registration/landlord/landlord_detail.html', {'landlord_detail': form})


# Zapisywanie formularza
def landlord_form_new(request):
    if request.method == "POST":
        form = LandlordsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/landlord/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = LandlordsForm()
        return render(request, 'registration/landlord/landlord_new.html', {'landlord_new': form})


# Edycja wpisu
def landlord_form_edit(request, pk):
    detail = get_object_or_404(Landlords, pk=pk)
    if request.method == "POST":
        form = LandlordsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/landlord/landlord_edit_success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = LandlordsForm(instance=detail)
    return render(request, 'registration/landlord/landlord_edit.html', {'landlord_edit': form})


def landlord_success(request):
    return render(request, 'registration/landlord/success.html', {'landlord_success': landlord_success})


##################
# Property methods
def property_list(request):
    form = Property.objects.all()
    return render(request, 'registration/prop/property_list.html', {'property_all': form})


def property_detail(request, pk):
    form = get_object_or_404(Property, pk=pk)
    return render(request, 'registration/prop/property_detail.html', {'property_detail': form})


# Zapisywanie formularza
def property_form_new(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/prop/property_new_success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = PropertyForm()
        return render(request, 'registration/prop/property_new.html', {'property_new': form})


# Edycja wpisu
def property_form_edit(request, pk):
    detail = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/prop/property_edit_success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = PropertyForm(instance=detail)
    return render(request, 'registration/prop/property_edit.html', {'property_edit': form})


def property_success(request):
    return render(request, 'registration/prop/success.html', {'property_success': property_success})


#########################
# Lease Agreement methods
def leaseagreement_list(request):
    form = LeaseAgreement.objects.all()
    return render(request, 'registration/lease/la_list.html', {'la_all': form})


def leaseagreement_detail(request, pk):
    form = get_object_or_404(LeaseAgreement, pk=pk)
    return render(request, 'registration/lease/la_detail.html', {'la_detail': form})


# Zapisywanie formularza
def leaseagreement_form_new(request):
    if request.method == "POST":
        form = LeaseAgreementForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/lease/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = LeaseAgreementForm()
        return render(request, 'registration/lease/la_new.html', {'la_new': form})


# Edycja wpisu
def leaseagreement_form_edit(request, pk):
    detail = get_object_or_404(LeaseAgreement, pk=pk)
    if request.method == "POST":
        form = LeaseAgreementForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/lease/la_edit_success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = LeaseAgreementForm(instance=detail)
    return render(request, 'registration/lease/la_edit.html', {'la_edit': form})


def leaseagreement_success(request):
    return render(request, 'registration/lease/success.html', {'la_success': leaseagreement_success})


#####################
# Bill Vendor methods
def billvendor_list(request):
    form = BillVendors.objects.all()
    return render(request, 'registration/vendor/vendor_list.html', {'billvendors_all': form})


def billvendor_detail(request, pk):
    form = get_object_or_404(BillVendors, pk=pk)
    return render(request, 'registration/vendor/vendor_detail.html', {'billvendor_detail': form})


# Zapisywanie formularza
def billvendor_form_new(request):
    if request.method == "POST":
        form = BillVendorsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/vendor/vendor_new_success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = BillVendorsForm()
        return render(request, 'registration/vendor/vendor_new.html', {'billvendor_new': form})


# Edycja wpisu
def billvendor_form_edit(request, pk):
    detail = get_object_or_404(BillVendors, pk=pk)
    if request.method == "POST":
        form = BillVendorsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/vendor/vendor_edit_success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = BillVendorsForm(instance=detail)
    return render(request, 'registration/vendor/vendor_edit.html', {'billvendor_edit': form})


def billvendor_success(request):
    return render(request, 'registration/vendor/success.html', {'billvendor_success': billvendor_success})


##############
# Bill methods
def bill_list(request):
    form = Bills.objects.all()
    return render(request, 'registration/bill/bill_list.html', {'bills_all': form})


def bill_detail(request, pk):
    form = get_object_or_404(Bills, pk=pk)
    return render(request, 'registration/bill/bill_detail.html', {'bill_detail': form})


# Zapisywanie formularza
def bill_form_new(request):
    if request.method == "POST":
        form = BillsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/bill/bill_new_success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = BillsForm()
        return render(request, 'registration/bill/bill_new.html', {'bill_new': form})


# Edycja wpisu
def bill_form_edit(request, pk):
    detail = get_object_or_404(Bills, pk=pk)
    if request.method == "POST":
        form = BillsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/bill/bill_edit_success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = BillsForm(instance=detail)
    return render(request, 'registration/bill/bill_edit.html', {'bill_edit': form})


def bill_success(request):
    return render(request, 'registration/bill/success.html', {'bill_success': bill_success})


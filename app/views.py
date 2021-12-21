from django.shortcuts import redirect, render, get_object_or_404
from .forms import *


def index(request):
    return render(request, 'registration/home.html')


def ha_list(request):
    form = HousingAssociation.objects.all()
    ha_count = HousingAssociation.objects.count()
    return render(request, 'registration/ha/ha_list.html', {'ha_all': form, 'ha_count': ha_count})


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


# Usuwanie wpisu
def housingassociation_delete(request, pk):
    ha = HousingAssociation.objects.get(id=pk)
    ha.delete()
    return housingassociation_success(request)


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
            return render(request, 'registration/tenants/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = TenantsForm(instance=detail)
    return render(request, 'registration/tenants/tenant_edit.html', {'tenant_edit': form})


# Usuwanie wpisu
def tenant_delete(request, pk):
    tenant = Tenants.objects.get(id=pk)
    tenant.delete()
    return tenant_success(request)


def tenant_success(request):
    return render(request, 'registration/tenants/success.html', {'tenant_success': tenant_success})


##################
# Landlord methods
def landlord_list(request):
    form = Landlords.objects.all()
    return render(request, 'registration/landlords/landlord_list.html', {'landlord_all': form})


def landlord_detail(request, pk):
    form = get_object_or_404(Landlords, pk=pk)
    return render(request, 'registration/landlords/landlord_detail.html', {'landlord_detail': form})


# Zapisywanie formularza
def landlord_form_new(request):
    if request.method == "POST":
        form = LandlordsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/landlords/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = LandlordsForm()
    return render(request, 'registration/landlords/landlord_new.html', {'landlord_new': form})


# Edycja wpisu
def landlord_form_edit(request, pk):
    detail = get_object_or_404(Landlords, pk=pk)
    if request.method == "POST":
        form = LandlordsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/landlords/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = LandlordsForm(instance=detail)
    return render(request, 'registration/landlords/landlord_edit.html', {'landlord_edit': form})


# Usuwanie wpisu
def landlord_delete(request, pk):
    landlord = Landlords.objects.get(id=pk)
    landlord.delete()
    return landlord_success(request)


def landlord_success(request):
    return render(request, 'registration/landlords/success.html', {'landlord_success': landlord_success})


##################
# Property methods
def property_list(request):
    form = Property.objects.all()
    prop_count = Property.objects.count()  # Zliczanie ilości obiektów w tablicy
    return render(request, 'registration/prop/prop_list.html', {'property_all': form, 'property_count': prop_count})


def property_detail(request, pk):
    form = get_object_or_404(Property, pk=pk)
    return render(request, 'registration/prop/prop_detail.html', {'property_detail': form})


# Zapisywanie formularza
def property_form_new(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/prop/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = PropertyForm()
    return render(request, 'registration/prop/prop_new.html', {'property_new': form})


# Edycja wpisu
def property_form_edit(request, pk):
    detail = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            # Property.objects.filter(id=pk).update(instance=detail)
            return render(request, 'registration/prop/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = PropertyForm(instance=detail)
    return render(request, 'registration/prop/prop_edit.html', {'property_edit': form})


# Usuwanie wpisu
def property_delete(request, pk):
    prop = Property.objects.get(id=pk)
    prop.delete()
    return property_success(request)


def property_success(request):
    return render(request, 'registration/prop/success.html', {'property_success': property_success})


#########################
# Lease Agreement methods
def leaseagreement_list(request):
    form = LeaseAgreement.objects.all()
    la_count = LeaseAgreement.objects.count()
    return render(request, 'registration/lease/la_list.html', {'la_all': form, 'la_count': la_count})


def leaseagreement_detail(request, pk):
    form = get_object_or_404(LeaseAgreement, pk=pk)
    return render(request, 'registration/lease/la_detail.html', {'leaseagreement_detail': form})


# Zapisywanie formularza
def leaseagreement_form_new(request):
    if request.method == "POST":
        form = LeaseAgreementForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/lease/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = LeaseAgreementForm()
    return render(request, 'registration/lease/la_new.html', {'leaseagreement_new': form})


# Edycja wpisu
def leaseagreement_form_edit(request, pk):
    detail = get_object_or_404(LeaseAgreement, pk=pk)
    if request.method == "POST":
        form = LeaseAgreementForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/lease/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = LeaseAgreementForm(instance=detail)
    return render(request, 'registration/lease/la_edit.html', {'leaseagreement_edit': form})


# Usuwanie wpisu
def leaseagreement_delete(request, pk):
    la = LeaseAgreement.objects.get(id=pk)
    la.delete()
    return leaseagreement_success(request)


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
            return render(request, 'registration/vendor/success.html') # Render strony po pomyślnym utworzeniu
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
            return render(request, 'registration/vendor/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = BillVendorsForm(instance=detail)
    return render(request, 'registration/vendor/vendor_edit.html', {'billvendor_edit': form})


# Usuwanie wpisu
def billvendor_delete(request, pk):
    billven = BillVendors.objects.get(id=pk)
    billven.delete()
    return billvendor_success(request)


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
            return render(request, 'registration/bill/success.html') # Render strony po pomyślnym utworzeniu
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
            return render(request, 'registration/bill/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = BillsForm(instance=detail)
    return render(request, 'registration/bill/bill_edit.html', {'bill_edit': form})


# Usuwanie wpisu
def bill_delete(request, pk):
    bill = Bills.objects.get(id=pk)
    bill.delete()
    return bill_success(request)


def bill_success(request):
    return render(request, 'registration/bill/success.html', {'bill_success': bill_success})


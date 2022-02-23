from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .forms import *


def index(request):
    return render(request, 'registration/home.html')


def error_400(request,  exception):
    data = {}
    return render(request, 'registration/400.html', data)


def error_404(request, exception):
    data = {}
    return render(request, 'registration/404.html', data)


def error_500(request):
    data = {}
    return render(request, 'registration/500.html', data)


def error_403(request,  exception):
    data = {}
    return render(request, 'registration/403.html', data)


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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('ha_list')
        messages.error(request, 'Błąd. Operacja nieudana.')
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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('ha_list')
        messages.error(request, 'Błąd. Operacja nieudana.')
    else:
        form = HousingAssociationForm(instance=detail)
    return render(request, 'registration/ha/ha_edit.html', {'ha_edit': form})


# Usuwanie wpisu
def housingassociation_delete(request, pk):
    ha = HousingAssociation.objects.get(id=pk)
    ha.delete()
    messages.success(request, 'Operacja wykonana pomyślnie')
    return redirect('ha_list')


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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('tenant_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('tenant_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
    else:
        form = TenantsForm(instance=detail)
    return render(request, 'registration/tenants/tenant_edit.html', {'tenant_edit': form})


# Usuwanie wpisu
def tenant_delete(request, pk):
    tenant = Tenants.objects.get(id=pk)
    tenant.delete()
    messages.success(request, 'Operacja wykonana pomyślnie')
    return redirect('tenant_all')


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
            # return render(request, 'registration/landlords/success.html')
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('landlord_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('landlord_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
    else:
        form = LandlordsForm(instance=detail)
    return render(request, 'registration/landlords/landlord_edit.html', {'landlord_edit': form})


# Usuwanie wpisu
def landlord_delete(request, pk):
    landlord = Landlords.objects.get(id=pk)
    landlord.delete()
    messages.success(request, 'Operacja wykonana pomyślnie')
    return redirect('landlord_all')


##################
# Property methods
def property_list(request):
    form = Property.objects.all()
    property_count = form.count()  # Zliczanie ilości obiektów w tablicy
    context = {
        'property_all': form,
        'property_count': property_count
    }
    return render(request, 'registration/prop/prop_list.html', context)


def property_detail(request, pk):
    form = get_object_or_404(Property, pk=pk)
    return render(request, 'registration/prop/prop_detail.html', {'property_detail': form})


# Zapisywanie formularza
def property_form_new(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('property_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('property_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
    else:
        form = PropertyForm(instance=detail)
    return render(request, 'registration/prop/prop_edit.html', {'property_edit': form})


# Usuwanie wpisu
def property_delete(request, pk):
    prop = Property.objects.get(id=pk)
    prop.delete()
    messages.success(request, 'Operacja wykonana pomyślnie')
    return redirect('property_all')


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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('leaseagreement_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('leaseagreement_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
    else:
        form = LeaseAgreementForm(instance=detail)
    return render(request, 'registration/lease/la_edit.html', {'leaseagreement_edit': form})


# Usuwanie wpisu
def leaseagreement_delete(request, pk):
    la = LeaseAgreement.objects.get(id=pk)
    la.delete()
    messages.success(request, 'Operacja wykonana pomyślnie')
    return redirect('leaseagreement_all')


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
            # return render(request, 'registration/vendor/success.html')
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('billvendor_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('billvendor_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
    else:
        form = BillVendorsForm(instance=detail)
    return render(request, 'registration/vendor/vendor_edit.html', {'billvendor_edit': form})


# Usuwanie wpisu
def billvendor_delete(request, pk):
    billven = BillVendors.objects.get(id=pk)
    billven.delete()
    messages.success(request, 'Operacja wykonana pomyślnie')
    return redirect('billvendor_all')


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
            # return render(request, 'registration/bill/success.html')
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('bill_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
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
            messages.success(request, 'Operacja wykonana pomyślnie')
            return redirect('bill_all')
        messages.error(request, 'Błąd. Operacja nieudana.')
    else:
        form = BillsForm(instance=detail)
    return render(request, 'registration/bill/bill_edit.html', {'bill_edit': form})


# Usuwanie wpisu
def bill_delete(request, pk):
    bill = Bills.objects.get(id=pk)
    bill.delete()
    messages.success(request, 'Operacja wykonana pomyślnie')
    return redirect('bill_all')


def summary_counters(request):
    ha_counter = HousingAssociation.objects.all().count()
    la_counter = LeaseAgreement.objects.all().count()
    property_counter = Property.objects.all().count()
    return render(request, 'registration/home.html', {'ha_counter': ha_counter,
                                                      'la_counter': la_counter,
                                                      'property_counter': property_counter})


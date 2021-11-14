from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from django.urls import reverse


def index(request):
    return render(request, 'registration/index.html')


# Housing Association methods
def ha_list(request):
    form = HousingAssociation.objects.all()
    return render(request, 'registration/ha_list.html', {'ha_all': form})


def housingassociation_detail(request, pk):
    form = get_object_or_404(HousingAssociation, pk=pk)
    return render(request, 'registration/ha_detail.html', {'ha_detail': form})


# Zapisywanie formularza
def housingassociation_form_new(request):
    if request.method == "POST":
        form = HousingAssociationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = HousingAssociationForm()
        return render(request, 'registration/ha_new.html', {'housingassociation_new': form})


# Edycja wpisu
def housingassociation_form_edit(request, pk):
    detail = get_object_or_404(HousingAssociation, pk=pk)
    if request.method == "POST":
        form = HousingAssociationForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = HousingAssociationForm(instance=detail)
    return render(request, 'registration/ha_edit.html', {'ha_edit': form})


def housingassociation_success(request):
    return render(request, 'registration/ha_success.html', {'ha_success': housingassociation_success})


# Tenants methods
def tenant_list(request):
    form = Tenants.objects.all()
    return render(request, 'registration/tenant_list.html', {'tenant_all': form})


def tenant_detail(request, pk):
    form = get_object_or_404(Tenants, pk=pk)
    return render(request, 'registration/tenant_detail.html', {'tenant_detail': form})


# Zapisywanie formularza
def tenant_form_new(request):
    if request.method == "POST":
        form = TenantsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/tenant_new_success.html') # Render strony po pomyślnym utworzeniu
    else:
        form = HousingAssociationForm()
        return render(request, 'registration/tenant_new.html', {'tenant_new': form})


# Edycja wpisu
def tenant_form_edit(request, pk):
    detail = get_object_or_404(Tenants, pk=pk)
    if request.method == "POST":
        form = TenantsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return render(request, 'registration/tenant_edit_success.html') # Render strony po pomyślnym zapisaniu
    else:
        form = TenantsForm(instance=detail)
    return render(request, 'registration/ha_edit.html', {'ha_edit': form})


def tenant_success(request):
    return render(request, 'registration/tenant_success.html', {'tenant_success': tenant_success})
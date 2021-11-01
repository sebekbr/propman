from django.shortcuts import redirect, render, get_object_or_404
from .forms import *


def index(request):
    # return HttpResponse("Hello, world. This is PropMan.")
    return render(request, 'registration/index.html')


# Widok nowego wpisu
# def housingassociation_form_new(request):
#     form = HousingAssociationForm()
#     return render(request, 'registration/form_edit.html', {'form': form})


def form_list(request):
    # form = get_object_or_404(HousingAssociationForm, pk=pk)
    return render(request, 'registration/ha_list.html')


def housingassociation_detail(request, pk):
    ha_detail = get_object_or_404(HousingAssociation, pk=pk)
    return render(request, 'registration/ha_detail.html', {'ha_detail': ha_detail})


# Zapisywanie formularza
def housingassociation_form_new(request):
    if request.method == "POST":
        form = HousingAssociationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('housingassociation_detail', pk=HousingAssociation.id)
    else:
        form = HousingAssociationForm()
        return render(request, 'registration/ha_new.html', {'housingassociation_new': form})


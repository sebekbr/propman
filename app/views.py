from django.shortcuts import redirect, render, get_object_or_404
from .forms import *


def index(request):
    # return HttpResponse("Hello, world. This is PropMan.")
    return render(request, 'propman/index.html')


# Widok nowego wpisu
# def housingassociation_form_new(request):
#     form = HousingAssociationForm()
#     return render(request, 'registration/form_edit.html', {'form': form})


def form_list(request):
    # form = get_object_or_404(HousingAssociationForm, pk=pk)
    return render(request, 'propman/ha_list.html')


def form_detail(request, pk):
    form = get_object_or_404(HousingAssociationForm, pk=pk)
    return render(request, 'propman/form_detail.html', {'form': form})


# Zapisywanie formularza
def housingassociation_form_new(request):
    if request.method == "POST":
        form = HousingAssociationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_detail', pk=HousingAssociation.id)
        else:
            form = HousingAssociationForm()
        return render(request, 'propman/form_edit.html', {'form': form})


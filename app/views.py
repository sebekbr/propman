from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from django.urls import reverse


def index(request):
    # return HttpResponse("Hello, world. This is PropMan.")
    return render(request, 'registration/index.html')


def form_list(request):
    ha_all = HousingAssociation.objects.all()
    return render(request, 'registration/ha_list.html', {'ha_all': ha_all})


def housingassociation_detail(request, pk):
    ha_detail = get_object_or_404(HousingAssociation, pk=pk)
    return render(request, 'registration/ha_detail.html', {'ha_detail': ha_detail})


# Zapisywanie formularza
def housingassociation_form_new(request):
    if request.method == "POST":
        form = HousingAssociationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ha_detail', pk=form.pk)
            # return redirect(reverse('ha_detail'), kwargs={'form': form.id})
    else:
        form = HousingAssociationForm()
        return render(request, 'registration/ha_new.html', {'housingassociation_new': form})


# Edycja wpisu
# def housingassociation_form_edit(request):
#     ha_detail = get_object_or_404(HousingAssociation, pk=pk)
#     if request.method == "POST":
#         form = HousingAssociationForm(request.POST, instance=ha_detail)
#         if form.is_valid():
#             ha_detail = form.save(commit=False)
#             ha_detail.name =
#             return redirect('housingassociation_detail', pk=HousingAssociation.pk)
#     else:
#         form = HousingAssociationForm()
#         return render(request, 'registration/ha_new.html', {'housingassociation_new': form})
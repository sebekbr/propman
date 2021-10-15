from django.shortcuts import render
from .forms import *


def index(request):
    # return HttpResponse("Hello, world. This is PropMan.")
    return render(request, 'registration/index.html')


# Widok nowego wpisu
def housingassociation_form_new(request):
    form_new = HousingAssociationForm()
    return render(request, 'registration/insert_test.html', {'form': form_new})


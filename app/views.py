from django.shortcuts import render
from .forms import HousingAssociationForm


def index(request):
    # return HttpResponse("Hello, world. This is PropMan.")
    return render(request, 'registration/index.html')


def form_new(request):
    form = HousingAssociationForm()
    return render(request, 'front/insert_test.html', {'form': form})


from django.shortcuts import render
from app.models import *


def counter(request):
    prop_count = Property.objects.count()  # Zliczanie ilości obiektów w tablicy
    return render(request, 'registration/prop/prop_list.html', {'property_count': prop_count})


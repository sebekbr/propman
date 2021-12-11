from django.shortcuts import render
from app.models import *


def counter(request):
    prop_count = Property.objects.count()
    la_count = LeaseAgreement.objects.count()
    hassoc_count = HousingAssociation.objects.count()
    return render(request, 'registration/ha/ha_list.html', {'property_count': prop_count,
                                                            'agreement_count': la_count,
                                                            'ha_count': hassoc_count})


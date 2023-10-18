from django.urls import path
from . import views


handler404 = 'app.views.error_404'
handler500 = 'app.views.error_500'
handler403 = 'app.views.error_403'
handler400 = 'app.views.error_400'


urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.summary_counters, name='summary_counters'),
    path('api', views.api_json, name='api'),
    path('api/', views.api_json, name='api'),

    # Housing Association
    path('forms/housingassociation/list', views.ha_list, name='ha_list'),
    path('forms/housingassociation/list/', views.ha_list, name='ha_list'),
    path('forms/housingassociation/new', views.housingassociation_form_new, name='housingassociation_new'), # definicja adresu URL nowego wpisu
    path('forms/housingassociation/new/', views.housingassociation_form_new, name='housingassociation_new'),
    path('forms/housingassociation/item/<int:pk>', views.housingassociation_detail, name='ha_detail'),
    path('forms/housingassociation/item/<int:pk>/', views.housingassociation_detail, name='ha_detail'),
    path('forms/housingassociation/item/<int:pk>/edit', views.housingassociation_form_edit, name='ha_edit'),
    path('forms/housingassociation/item/<int:pk>/edit/', views.housingassociation_form_edit, name='ha_edit'),
    path('forms/housingassociation/item/<int:pk>/del', views.housingassociation_delete, name='ha_delete'),
    path('forms/housingassociation/item/<int:pk>/del/', views.housingassociation_delete, name='ha_delete'),

    # Tenants
    path('forms/tenant/list', views.tenant_list, name='tenant_all'),
    path('forms/tenant/list/', views.tenant_list, name='tenant_all'),
    path('forms/tenant/new', views.tenant_form_new, name='tenant_new'), # definicja adresu URL nowego wpisu
    path('forms/tenant/new/', views.tenant_form_new, name='tenant_new'),
    path('forms/tenant/item/<int:pk>', views.tenant_detail, name='tenant_detail'),
    path('forms/tenant/item/<int:pk>/', views.tenant_detail, name='tenant_detail'),
    path('forms/tenant/item/<int:pk>/edit', views.tenant_form_edit, name='tenant_edit'),
    path('forms/tenant/item/<int:pk>/edit/', views.tenant_form_edit, name='tenant_edit'),
    path('forms/tenant/item/<int:pk>/del', views.tenant_delete, name='tenant_delete'),
    path('forms/tenant/item/<int:pk>/del/', views.tenant_delete, name='tenant_delete'),

    # Landlords
    path('forms/landlord/list', views.landlord_list, name='landlord_all'),
    path('forms/landlord/list/', views.landlord_list, name='landlord_all'),
    path('forms/landlord/new', views.landlord_form_new, name='landlord_new'), # definicja adresu URL nowego wpisu
    path('forms/landlord/new/', views.landlord_form_new, name='landlord_new'),
    path('forms/landlord/item/<int:pk>', views.landlord_detail, name='landlord_detail'),
    path('forms/landlord/item/<int:pk>/', views.landlord_detail, name='landlord_detail'),
    path('forms/landlord/item/<int:pk>/edit', views.landlord_form_edit, name='landlord_edit'),
    path('forms/landlord/item/<int:pk>/edit/', views.landlord_form_edit, name='landlord_edit'),
    path('forms/landlord/item/<int:pk>/delete', views.landlord_delete, name='landlord_delete'),
    path('forms/landlord/item/<int:pk>/delete/', views.landlord_delete, name='landlord_delete'),

    # Property
    path('forms/property/list', views.property_list, name='property_all'),
    path('forms/property/list/', views.property_list, name='property_all'),
    path('forms/property/new', views.property_form_new, name='property_new'), # definicja adresu URL nowego wpisu
    path('forms/property/new/', views.property_form_new, name='property_new'),
    path('forms/property/item/<int:pk>', views.property_detail, name='property_detail'),
    path('forms/property/item/<int:pk>/', views.property_detail, name='property_detail'),
    path('forms/property/item/<int:pk>/edit', views.property_form_edit, name='property_edit'),
    path('forms/property/item/<int:pk>/edit/', views.property_form_edit, name='property_edit'),
    path('forms/property/item/<int:pk>/del', views.property_delete, name='property_delete'),
    path('forms/property/item/<int:pk>/del/', views.property_delete, name='property_delete'),

    # Lease Agreements
    path('forms/leaseagreement/list', views.leaseagreement_list, name='leaseagreement_all'),
    path('forms/leaseagreement/list/', views.leaseagreement_list, name='leaseagreement_all'),
    path('forms/leaseagreement/new', views.leaseagreement_form_new, name='leaseagreement_new'), # definicja adresu URL nowego wpisu
    path('forms/leaseagreement/new/', views.leaseagreement_form_new, name='leaseagreement_new'),
    path('forms/leaseagreement/item/<int:pk>', views.leaseagreement_detail, name='leaseagreement_detail'),
    path('forms/leaseagreement/item/<int:pk>/', views.leaseagreement_detail, name='leaseagreement_detail'),
    path('forms/leaseagreement/item/<int:pk>/edit', views.leaseagreement_form_edit, name='leaseagreement_edit'),
    path('forms/leaseagreement/item/<int:pk>/edit/', views.leaseagreement_form_edit, name='leaseagreement_edit'),
    path('forms/leaseagreement/item/<int:pk>/del', views.leaseagreement_delete, name='leaseagreement_delete'),
    path('forms/leaseagreement/item/<int:pk>/del/', views.leaseagreement_delete, name='leaseagreement_delete'),

    # Bill Vendors
    path('forms/billven/list', views.billvendor_list, name='billvendor_all'),
    path('forms/billven/list/', views.billvendor_list, name='billvendor_all'),
    path('forms/billven/new', views.billvendor_form_new, name='billvendor_new'), # definicja adresu URL nowego wpisu
    path('forms/billven/new/', views.billvendor_form_new, name='billvendor_new'),
    path('forms/billven/item/<int:pk>', views.billvendor_detail, name='billvendor_detail'),
    path('forms/billven/item/<int:pk>/', views.billvendor_detail, name='billvendor_detail'),
    path('forms/billven/item/<int:pk>/edit', views.billvendor_form_edit, name='billvendor_edit'),
    path('forms/billven/item/<int:pk>/edit/', views.billvendor_form_edit, name='billvendor_edit'),
    path('forms/billven/item/<int:pk>/del', views.billvendor_delete, name='billvendor_delete'),
    path('forms/billven/item/<int:pk>/del/', views.billvendor_delete, name='billvendor_delete'),

    # Bills
    path('forms/bill/list', views.bill_list, name='bill_all'),
    path('forms/bill/list/', views.bill_list, name='bill_all'),
    path('forms/bill/new', views.bill_form_new, name='bill_new'), # definicja adresu URL nowego wpisu
    path('forms/bill/new/', views.bill_form_new, name='bill_new'),
    path('forms/bill/item/<int:pk>', views.bill_detail, name='bill_detail'),
    path('forms/bill/item/<int:pk>/', views.bill_detail, name='bill_detail'),
    path('forms/bill/item/<int:pk>/edit', views.bill_form_edit, name='bill_edit'),
    path('forms/bill/item/<int:pk>/edit/', views.bill_form_edit, name='bill_edit'),
    path('forms/bill/item/<int:pk>/del', views.bill_delete, name='bill_delete'),
    path('forms/bill/item/<int:pk>/del/', views.bill_delete, name='bill_delete'),

    #
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('join/', views.SignupView.as_view(), name='join'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Housing Association
    path('forms/housingassociation/list', views.ha_list, name='ha_list'),
    path('forms/housingassociation/list/', views.ha_list, name='ha_list'),
    path('forms/housingassociation/new', views.housingassociation_form_new, name='housingassociation_new'), # definicja adresu URL nowego wpisu
    path('forms/housingassociation/new/', views.housingassociation_form_new, name='housingassociation_new'),
    path('forms/housingassociation/item/<int:pk>', views.housingassociation_detail, name='ha_detail'),
    path('forms/housingassociation/item/<int:pk>/', views.housingassociation_detail, name='ha_detail'),
    path('forms/housingassociation/item/<int:pk>/edit', views.housingassociation_form_edit, name='ha_edit'),
    path('forms/housingassociation/item/<int:pk>/edit/', views.housingassociation_form_edit, name='ha_edit'),
    path('forms/housingassociation/success', views.housingassociation_success, name='ha_success'),

    # Tenants
    path('forms/tenant/list', views.tenant_list, name='tenant_all'),
    path('forms/tenant/list/', views.tenant_list, name='tenant_all'),
    path('forms/tenant/new', views.tenant_form_new, name='tenant_new'), # definicja adresu URL nowego wpisu
    path('forms/tenant/new/', views.tenant_form_new, name='tenant_new'),
    path('forms/tenant/item/<int:pk>', views.tenant_detail, name='tenant_detail'),
    path('forms/tenant/item/<int:pk>/', views.tenant_detail, name='tenant_detail'),
    path('forms/tenant/item/<int:pk>/edit', views.tenant_form_edit, name='tenant_edit'),
    path('forms/tenant/item/<int:pk>/edit/', views.tenant_form_edit, name='tenant_edit'),
    path('forms/tenant/success', views.tenant_success, name='tenant_success'),

    # Landlords
    path('forms/landlord/list', views.landlord_list, name='landlord_list'),
    path('forms/landlord/list/', views.landlord_list, name='landlord_list'),
    path('forms/landlord/new', views.landlord_form_new, name='landlord_new'), # definicja adresu URL nowego wpisu
    path('forms/landlord/new/', views.landlord_form_new, name='landlord_new'),
    path('forms/landlord/item/<int:pk>', views.landlord_detail, name='landlord_detail'),
    path('forms/landlord/item/<int:pk>/', views.landlord_detail, name='landlord_detail'),
    path('forms/landlord/item/<int:pk>/edit', views.landlord_form_edit, name='landlord_edit'),
    path('forms/landlord/item/<int:pk>/edit/', views.landlord_form_edit, name='landlord_edit'),
    path('forms/landlord/success', views.landlord_success, name='landlord_success'),

    # Property
    path('forms/property/list', views.property_list, name='property_list'),
    path('forms/property/list/', views.property_list, name='property_list'),
    path('forms/property/new', views.property_form_new, name='property_new'), # definicja adresu URL nowego wpisu
    path('forms/property/new/', views.property_form_new, name='property_new'),
    path('forms/property/item/<int:pk>', views.property_detail, name='property_detail'),
    path('forms/property/item/<int:pk>/', views.property_detail, name='property_detail'),
    path('forms/property/item/<int:pk>/edit', views.property_form_edit, name='property_edit'),
    path('forms/property/item/<int:pk>/edit/', views.property_form_edit, name='property_edit'),
    path('forms/property/success', views.property_success, name='property_success'),

    # Lease Agreements
    path('forms/leaseagreement/list', views.leaseagreement_list, name='leaseagreement_list'),
    path('forms/leaseagreement/list/', views.leaseagreement_list, name='leaseagreement_list'),
    path('forms/leaseagreement/new', views.leaseagreement_form_new, name='leaseagreement_new'), # definicja adresu URL nowego wpisu
    path('forms/leaseagreement/new/', views.leaseagreement_form_new, name='leaseagreement_new'),
    path('forms/leaseagreement/item/<int:pk>', views.leaseagreement_detail, name='leaseagreement_detail'),
    path('forms/leaseagreement/item/<int:pk>/', views.leaseagreement_detail, name='leaseagreement_detail'),
    path('forms/leaseagreement/item/<int:pk>/edit', views.leaseagreement_form_edit, name='leaseagreement_edit'),
    path('forms/leaseagreement/item/<int:pk>/edit/', views.leaseagreement_form_edit, name='leaseagreement_edit'),
    path('forms/leaseagreement/success', views.leaseagreement_success, name='leaseagreement_success'),

    # Bill Vendors
    path('forms/billven/list', views.billvendor_list, name='billvendor_list'),
    path('forms/billven/list/', views.billvendor_list, name='billvendor_list'),
    path('forms/billven/new', views.billvendor_form_new, name='billvendor_new'), # definicja adresu URL nowego wpisu
    path('forms/billven/new/', views.billvendor_form_new, name='billvendor_new'),
    path('forms/billven/item/<int:pk>', views.billvendor_detail, name='billvendor_detail'),
    path('forms/billven/item/<int:pk>/', views.billvendor_detail, name='billvendor_detail'),
    path('forms/billven/item/<int:pk>/edit', views.billvendor_form_edit, name='billvendor_edit'),
    path('forms/billven/item/<int:pk>/edit/', views.billvendor_form_edit, name='billvendor_edit'),
    path('forms/billven/success', views.billvendor_success, name='billvendor_success'),

    # Bills
    path('forms/bill/list', views.bill_list, name='bill_list'),
    path('forms/bill/list/', views.bill_list, name='bill_list'),
    path('forms/bill/new', views.bill_form_new, name='bill_new'), # definicja adresu URL nowego wpisu
    path('forms/bill/new/', views.bill_form_new, name='bill_new'),
    path('forms/bill/item/<int:pk>', views.bill_detail, name='bill_detail'),
    path('forms/bill/item/<int:pk>/', views.bill_detail, name='bill_detail'),
    path('forms/bill/item/<int:pk>/edit', views.bill_form_edit, name='bill_edit'),
    path('forms/bill/item/<int:pk>/edit/', views.bill_form_edit, name='bill_edit'),
    path('forms/bill/success', views.bill_success, name='bill_success')

    #
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('join/', views.SignupView.as_view(), name='join'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
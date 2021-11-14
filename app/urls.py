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
    path('forms/tenant/list', views.tenant_list, name='tenant_list'),
    path('forms/tenant/list/', views.tenant_list, name='tenant_list'),
    path('forms/tenant/new', views.tenant_form_new, name='tenant_new'), # definicja adresu URL nowego wpisu
    path('forms/tenant/new/', views.tenant_form_new, name='tenant_new'),
    path('forms/tenant/item/<int:pk>', views.tenant_detail, name='tenant_detail'),
    path('forms/tenant/item/<int:pk>/', views.tenant_detail, name='tenant_detail'),
    path('forms/tenant/item/<int:pk>/edit', views.tenant_form_edit, name='tenant_edit'),
    path('forms/tenant/item/<int:pk>/edit/', views.tenant_form_edit, name='tenant_edit'),
    path('forms/tenant/success', views.tenant_success, name='tenant_success')

    # Landlords

    # Property

    # Lease Agreements

    # Bill Vendors

    # Bills

    #
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('join/', views.SignupView.as_view(), name='join'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/housingassociation/list', views.form_list, name='ha_list'),
    path('forms/housingassociation/item/<int:pk>', views.housingassociation_detail, name='ha_detail'),
    path('forms/housingassociation/new', views.housingassociation_form_new, name='housingassociation_new'), # definicja adresu URL nowego wpisu
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('join/', views.SignupView.as_view(), name='join'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
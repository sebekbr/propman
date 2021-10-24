from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/list', views.form_list, name='ha_list'),
    path('forms/<int:pk>/', views.form_detail, name='form_detail'),
    path('forms/new', views.housingassociation_form_new, name='form_new'), # definicja adresu URL nowego wpisu
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('join/', views.SignupView.as_view(), name='join'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
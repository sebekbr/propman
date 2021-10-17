from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/list', views.form_list, name='ha_list'),
    path('forms/<int:pk>/', views.form_detail, name='form_detail'),
    path('forms/new', views.housingassociation_form_new, name='form_new'), # definicja adresu URL nowego wpisu
]
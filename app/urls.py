from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.form_detail, name='form_detail'),
    path('forms/new', views.housingassociation_form_new, name='form'), # definicja adresu URL nowego wpisu
]
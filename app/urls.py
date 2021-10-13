from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/new', views.form_new, name='form_new'),
]
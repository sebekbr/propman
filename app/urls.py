from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
]


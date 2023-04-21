from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.compound_interest, name='compound_interest'),
]

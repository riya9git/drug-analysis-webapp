from django.urls import path
from . import views

urlpatterns = [
    path('', views.drug_summary, name='summary'),
]

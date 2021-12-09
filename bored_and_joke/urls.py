from django.urls import path
from .views import get_bored_and_joke, bored_csv

urlpatterns = [
    path('boredandjoke/<str:tipo>', get_bored_and_joke, name='get_bored_and_joke'),
    path('all', bored_csv, name='bored_csv'),
    ]
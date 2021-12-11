from django.urls import path
from .views import bored_csv, BoredAndJokeView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
urlpatterns = [
    #path('api/<str:tipo>', get_bored_and_joke, name='get_bored_and_joke'),
    path('all', bored_csv, name='bored_csv'),
    path('api/<str:tipo>', BoredAndJokeView.as_view(), name='get_bored_and_joke'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]
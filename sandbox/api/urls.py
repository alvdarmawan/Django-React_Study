from django.urls import path
from .views import ahoj

urlpatterns = [
    path('dobry_den/', ahoj),
    path('', ahoj)
]
from django.urls import path

# app
from .views import create_index

urlpatterns = [
  path('', create_index)
]
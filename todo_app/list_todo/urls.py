from django.urls import path

# app
from .views import list_index

urlpatterns = [
  path('', list_index)
]
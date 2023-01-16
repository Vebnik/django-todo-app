from django.urls import path

from .views import get_todo

urlpatterns = [
  path('todo', get_todo)
]
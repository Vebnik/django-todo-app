# std
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('list_todo.urls')),
    path('create/', include('create_todo.urls')),
]

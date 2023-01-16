# std
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('list_todo.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls'))
]

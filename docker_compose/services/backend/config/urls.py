from django.contrib import admin
from django.urls import include, path
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += []

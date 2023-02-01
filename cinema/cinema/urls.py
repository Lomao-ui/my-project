
from django.contrib import admin
from django.urls import path, include
from kino.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kino.urls')),
]

handler404 = pageNotFound
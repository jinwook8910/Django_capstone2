from main.views import index
from main.views import index2
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
   path('checkip/', index2),
]

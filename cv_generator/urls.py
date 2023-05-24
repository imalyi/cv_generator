
from django.contrib import admin
from django.urls import path
import cv_generator.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register", views.register_request, name="register")
]

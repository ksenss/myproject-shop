from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("details/", views.details),
    path("delete/<int:id>", views.delete),
]
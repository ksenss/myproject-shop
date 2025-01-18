from django.contrib import admin
from django.urls import include, path

from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("details/<int:id>", views.details),
    path("", views.index),
    path("create/", views.create),
    path("delete/<int:id>", views.delete),
    path("edit/<int:id>", views.edit),
]
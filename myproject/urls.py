from django.contrib import admin
from django.urls import include, path

from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("details/<int:id>", views.details),
    path('', views.index, name='index'),
    path("create/", views.create),
    path("delete/<int:id>", views.delete),
    path("edit/<int:id>", views.edit),
    path('cart/', views.view_cart, name='cart'),  # Перегляд корзини
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Додавання товару в корзину
    path('cart/update/<int:cart_id>/', views.update_cart, name='update_cart'),  # Оновлення кількості товару
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),  # Видалення товару з корзини
]
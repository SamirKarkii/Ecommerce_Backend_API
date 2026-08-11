from django.urls import path
from .views import ProductView, ProductDetailView, CategoryView, CategoryDetailView



urlpatterns = [
    path("products/",ProductView.as_view(),name="product-list"),
    path("categories/",CategoryView.as_view(),name="category-list"),
    path( "products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("categories/<int:pk>/",CategoryDetailView.as_view(), name="category-detail")
]


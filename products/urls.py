from django.urls import path
from . import views


urlpatterns = [
    path("products/list", views.ProductListView.as_view(), name="Product_list"),
    path("products/create", views.ProductCreateView.as_view(), name="Product_create"),
    path("products/<int:pk>/detail", views.ProductDetailView.as_view(), name="Product_detail"),
    path("products/<int:pk>/update", views.ProductUpdateView.as_view(), name="Product_update"),
    path("products/<int:pk>/delete", views.ProductDeleteView.as_view(), name="Product_delete"),
]
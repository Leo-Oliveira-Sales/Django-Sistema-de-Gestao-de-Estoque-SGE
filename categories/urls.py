from django.urls import path
from . import views


urlpatterns = [
    path("categories/list", views.CategoryListView.as_view(), name="Category_list"),
    path("categories/create", views.CategoryCreateView.as_view(), name="Category_create"),
    path("categories/<int:pk>/detail", views.CategoryDetailView.as_view(), name="Category_detail"),
    path("categories/<int:pk>/update", views.CategoryUpdateView.as_view(), name="Category_update"),
    path("categories/<int:pk>/delete", views.CategoryDeleteView.as_view(), name="Category_delete"),

    path("api/av1/categories", views.CategoryCreateListAPIView.as_view(), name="category_create_list_api_view"),
    path("api/av1/categories/<int:pk>", views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category_detail_api_view"),
]

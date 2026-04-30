from django.urls import path
from . import views


urlpatterns = [
    path("categories/list", views.CategoryListView.as_view(), name="Category_list"),
    path("categories/create", views.CategoryCreateView.as_view(), name="Category_create"),
    path("categories/<int:pk>/detail", views.CategoryDetailView.as_view(), name="Category_detail"),
    path("categories/<int:pk>/update", views.CategoryUpdateView.as_view(), name="Category_update"),
    path("categories/<int:pk>/delete", views.CategoryDeleteView.as_view(), name="Category_delete"),
]

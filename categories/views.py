# from typing import Any
# from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = "Category_list.html"
    context_object_name = "Categories"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    template_name = "Category_create.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("Category_list")

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category
    template_name = "Category_detail.html"

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    template_name = "Category_update.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("Category_list")

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = "Category_delete.html"
    success_url = reverse_lazy("Category_list")

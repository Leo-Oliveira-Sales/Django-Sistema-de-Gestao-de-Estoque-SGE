from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class ProductListView(ListView):
    model = models.Product
    template_name = "Product_list.html"
    context_object_name = "Products"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get("title")

        if title:
            queryset = queryset.filter(name__icontains=title)
        return queryset

class ProductCreateView(CreateView):
    model = models.Product
    template_name = "Product_create.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("Product_list")

class ProductDetailView(DetailView):
    model = models.Product
    template_name = "Product_detail.html"

class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = "Product_update.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("Product_list")

class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = "Product_delete.html"
    success_url = reverse_lazy("Product_list")

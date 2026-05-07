# from typing import Any
# from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class SupplierListView(LoginRequiredMixin, ListView):
    model = models.Supplier
    template_name = "Supplier_list.html"
    context_object_name = "Suppliers"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = models.Supplier
    template_name = "Supplier_create.html"
    form_class = forms.SupplierForm
    success_url = reverse_lazy("Supplier_list")

class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = models.Supplier
    template_name = "Supplier_detail.html"

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Supplier
    template_name = "Supplier_update.html"
    form_class = forms.SupplierForm
    success_url = reverse_lazy("Supplier_list")

class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = "Supplier_delete.html"
    success_url = reverse_lazy("Supplier_list")        

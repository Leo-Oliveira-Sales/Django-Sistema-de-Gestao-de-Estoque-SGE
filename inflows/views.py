from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class InflowListView(ListView):
    model = models.Inflow
    template_name = "Inflow_list.html"
    context_object_name = "Inflows"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset

class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = "Inflow_create.html"
    form_class = forms.InflowForm
    success_url = reverse_lazy("Inflow_list")

class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = "Inflow_detail.html"

from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class OutflowListView(ListView):
    model = models.Outflow
    template_name = "Outflow_list.html"
    context_object_name = "Outflows"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset

class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = "Outflow_create.html"
    form_class = forms.OutflowForm
    success_url = reverse_lazy("Outflow_list")

class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = "Outflow_detail.html"

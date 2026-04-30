from django.urls import path
from . import views


urlpatterns = [
    path("outflows/list", views.OutflowListView.as_view(), name="Outflow_list"),
    path("outflows/create", views.OutflowCreateView.as_view(), name="Outflow_create"),
    path("outflows/<Out:pk>/detail", views.OutflowDetailView.as_view(), name="Outflow_detail"),
]

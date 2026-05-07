from django.urls import path
from . import views


urlpatterns = [
    path("outflows/list", views.OutflowListView.as_view(), name="Outflow_list"),
    path("outflows/create", views.OutflowCreateView.as_view(), name="Outflow_create"),
    path("outflows/<int:pk>/detail", views.OutflowDetailView.as_view(), name="Outflow_detail"),

    path("api/av1/outflows", views.OutflowCreateListAPIView.as_view(), name="outflow_create_list_api_view"),
    path("api/av1/outflows/<int:pk>", views.OutflowRetrieveAPIView.as_view(), name="outflow_detail_api_view"),
]

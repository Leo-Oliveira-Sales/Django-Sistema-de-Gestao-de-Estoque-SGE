from django.urls import path
from . import views


urlpatterns = [
    path("inflows/list", views.InflowListView.as_view(), name="Inflow_list"),
    path("inflows/create", views.InflowCreateView.as_view(), name="Inflow_create"),
    path("inflows/<int:pk>/detail", views.InflowDetailView.as_view(), name="Inflow_detail"),

    path("api/av1/inflows", views.InflowCreateListAPIView.as_view(), name="inflow_create_list_api_view"),
    path("api/av1/inflows/<int:pk>", views.InflowRetrieveAPIView.as_view(), name="inflow_detail_api_view"),
]
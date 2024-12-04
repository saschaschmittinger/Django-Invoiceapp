from django.urls import path
from .views import (
    Home_base_view,
    InvoiceFormView,
    SimpleTemplateView,
    InvoiceUpdateView,
    AddPositionsFormView,
)


app_name = "invoices"

urlpatterns = [
    path("", Home_base_view.as_view(), name="base_view"),
    path("create/", InvoiceFormView.as_view(), name="invoiceFormView"),
    # path("<pk>/", SimpleTemplateView.as_view(), name="simpleTemplateView"),
    path("<pk>/update/", InvoiceUpdateView.as_view(), name="InvoiceUpdateView"),
    path(
        "<pk>/",
        AddPositionsFormView.as_view(),
        name="AddPositionsFormView",
    ),
]

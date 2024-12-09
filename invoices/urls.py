from django.urls import path
from .views import (
    Home_base_view,
    InvoiceFormView,
    InvoiceUpdateView,
    AddPositionsFormView,
    CloseInvoiceView,
    InvoicePositionDeleteView,
)


app_name = "invoices"

urlpatterns = [
    path("", Home_base_view.as_view(), name="base_view"),
    path("create/", InvoiceFormView.as_view(), name="invoiceFormView"),
    path("<pk>/close/", CloseInvoiceView.as_view(), name="closeInvoiceView"),
    path("<pk>/update/", InvoiceUpdateView.as_view(), name="InvoiceUpdateView"),
    path(
        "<pk>/",
        AddPositionsFormView.as_view(),
        name="AddPositionsFormView",
    ),
    path(
        "<pk>/delete/<int:position_pk>/",
        InvoicePositionDeleteView.as_view(),
        name="InvoicePositionDeleteView",
    ),
]

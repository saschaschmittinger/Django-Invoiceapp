from django.urls import path
from .views import Home_base_view


app_name = "invoices"

urlpatterns = [path("", Home_base_view.as_view(), name="base_view")]

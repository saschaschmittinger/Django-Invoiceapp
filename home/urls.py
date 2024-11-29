from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import hello_world


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls", namespace="profiles")),
    path("hallo/", hello_world, name="hello_world"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# optische Änderung des Admin-Pannels

admin.site.site_header = "SSC Admin"
admin.site.site_title = "SSC Admin"

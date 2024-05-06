from django.contrib import admin
from django.urls import path
from newss.views import HealthCheckView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HealthCheckView.as_view()),
]

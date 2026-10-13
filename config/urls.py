from django.urls import path

from app.views import ping

urlpatterns = [
    path("api/ping/", ping),
]

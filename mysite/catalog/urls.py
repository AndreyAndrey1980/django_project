from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact_info", views.get_contact_info, name="get_contact_info")
]

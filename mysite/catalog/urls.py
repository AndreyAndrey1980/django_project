from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "catalog"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.detail, name='detail'),
    path("contact_info", views.get_contact_info, name="get_contact_info")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
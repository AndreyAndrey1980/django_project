from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "catalog"
urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name='detail'),
    path("contact", views.GetContact.as_view(), name="contact"),
    path("<int:pk>/delete", views.ProductDeleteView.as_view(), name="delete"),
    path("create", views.ProductCreateView.as_view(), name="create"),
    path("<int:pk>/update", views.ProductUpdateView.as_view(), name="update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

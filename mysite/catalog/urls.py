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
    path("blog/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", views.BlogDetailView.as_view(), name='blog_detail'),
    path("blog/<slug:slug>/delete", views.BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/create", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/<slug:slug>/update", views.BlogUpdateView.as_view(), name="blog_update"),
    path("create-version", views.VersionCreateView.as_view(), name="create_version"),
    path("<int:pk>/update-version", views.ProductUpdateView.as_view(), name="update_version"),
    path("<int:pk>/delete_version", views.VersionDeleteView.as_view(), name="delete_version")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

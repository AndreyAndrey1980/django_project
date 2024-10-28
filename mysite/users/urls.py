from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name = "users"
urlpatterns = [
    path("register", views.UserRegisterView.as_view(success_url='/catalog'), name="users_register"),
    path("login", views.UserLoginView.as_view(), name="users_login"),
    path("logout", LogoutView.as_view(), name="users_logout"),
    path("pass_rec", views.ResetPassword.as_view(), name="recovery_password")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
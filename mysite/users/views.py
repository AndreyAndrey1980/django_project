from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import User
from django.views.generic.edit import FormView
from .forms import RegisterForm, EmailForm
from django.conf import settings
from django.core.mail import send_mail
import string
import random


class UserRegisterView(CreateView):
    # Создаем обычный контроллер на создание сущности
    model = User
    form_class = RegisterForm

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            print(new_user.email)
            print(settings.EMAIL_HOST_USER)
            send_mail('Регистрация', 'Регистрация прошла успешно',
                      settings.EMAIL_HOST_USER, [new_user.email])
            print("cообщение отправлено на почту")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "login.html"


class ResetPassword(FormView):
    form_class = EmailForm
    template_name = "password_reset.html"
    success_url = "/catalog"

    def form_valid(self, form):
        if form.is_valid():
            print(type(form))
            print(form)
            email = form.cleaned_data["email"]
            user = User.objects.get(email=email)
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            user.set_password(password)
            user.save(update_fields=['password'])
            send_mail('Сброс пароля', f'ваш новый пароль {password}',
                      settings.EMAIL_HOST_USER, [user.email])

        return super().form_valid(form)

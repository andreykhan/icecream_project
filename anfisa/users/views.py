from django.views.generic import CreateView # Импортируем CreateView, чтобы создать ему наследника

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

from .forms import CreationForm # Импортируем класс формы, чтобы сослаться на неё во view-классе


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')  # После успешной регистрации перенаправляем пользователя на главную.
    template_name = 'users/signup.html'
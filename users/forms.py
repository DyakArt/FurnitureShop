from django import forms
# форма django, которая проверяет всё для авторизации пользователя
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


# создаем и описываем форму входа, чтобы применить валидацию к полям
class UserLoginForm(AuthenticationForm):
    # лучше делать так, закомментировано, так как эти поля уже есть в классе AuthenticationForm
    # username = forms.CharField()
    # password = forms.CharField()
    class Meta:
        # указываем с какой моделью будет работать форма AuthenticationForm - это User, чтобы подтянуть все правила
        # этой модели, нужно для правильной валидации в контроллере
        model = User
        # указываем какие поля отображать
        fields = ['username', 'password']

    # второй вариант
    # указываем как отображать поле username
    # widgets - как будут отображаться поля и реагировать
    # username = forms.CharField(
    #     label='Имя пользователя:',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введите имя пользователя'}))
    # # указываем как отображать поле password
    # password = forms.CharField(
    #     label='Пароль:',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введите ваш пароль'}),
    # )

from django import forms
# форма django, которая проверяет всё для авторизации пользователя и создания пользователя
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


# создаем и описываем форму входа, чтобы применить валидацию к полям
class UserLoginForm(AuthenticationForm):
    # лучше делать этот вариант
    # закомментировано, так как эти поля уже есть в классе AuthenticationForm
    # username = forms.CharField()
    # password = forms.CharField()
    class Meta:
        # указываем с какой моделью будет работать форма AuthenticationForm - это User, чтобы подтянуть все правила
        # этой модели, нужно для правильной валидации в контроллере
        model = User
        # указываем какие поля отображать это берётся из AuthenticationForm и модели, которую ты указал
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


# создаем и описываем форму регистрации, чтобы применить валидацию к полям
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        # указываем какие поля отображать
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2')

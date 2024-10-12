from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import redirect

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    # если POST-запрос, (пользователь нажал на кнопку "Войти" на POST форме)
    # каждый раз при запрашивании страницы CSRF-токен будет генерироваться заново, чтобы убедиться, что
    # информация, которая придёт в контроллер отправлена именно ЭТИМ пользователем
    # это защита от сайтов-подделок и перехвата данных
    if request.method == 'POST':
        # создаём форму и наполняем её данными, которые ввёл пользователь в input-тегах
        form = UserLoginForm(data=request.POST)
        # если форма валидна
        if form.is_valid():
            # названия (name) input-полей берутся из модели БД, которая связана с формой
            username = request.POST['username']
            password = request.POST['password']
            # сначала аутентификация
            # authenticate - метод, который проверяет есть ли такой пользователь в БД, если есть, то
            # вернется объект user
            user = auth.authenticate(username=username, password=password)
            # если вернулся объект user, то тогда авторизуем его
            if user:
                auth.login(request, user)
                # перенаправляем пользователя на главную страницу нашего сайта
                # с помощью reverse (как это делается в шаблонах)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        # если GET-запрос, то формируем пустую форму (при обычном заходе на страницу)
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        # если форма валидна, то сохраняем данные из формы в БД и создаем нового пользователя
        if form.is_valid():
            form.save()
            # получаем все атрибуты пользователя из формы
            user = form.instance
            # авторизуем пользователя через эти атрибуты
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Профиль'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    # выходим из аккаунта
    auth.logout(request)
    # перенаправляем на главную страницу
    return redirect(reverse('main:index'))

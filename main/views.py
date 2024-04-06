from django.shortcuts import render
from django.http import HttpResponse

# импортируем модель Categories из приложения товаров
from goods.models import Categories

# в этом файле все функции называются либо представления, либо контроллеры
# после создания, нужно закрепить её за каким-нибудь url-адресом

"""
Функция, которая обрабатывает запросы на главную страницу нашего сайта
В параметр request попадает экземпляр класса http-request,
он содержит в себе все данные о запросе (зарегистрированный пользователь или анонимный, файлы cookies,
метод запроса (GET/POST) и тд)
"""


def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)


# представление для страницы "о нас"
def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классный.'
    }
    return render(request, 'main/about.html', context)

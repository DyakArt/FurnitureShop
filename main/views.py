from django.shortcuts import render
from django.http import HttpResponse

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
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)


# представление для страницы "о нас"
def about(request) -> HttpResponse:
    return HttpResponse('About page')

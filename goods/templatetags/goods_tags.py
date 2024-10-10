# импортируем template
from django import template
from django.utils.http import urlencode

# импортируем модель категорий товаров
from goods.models import Categories

# регистрируем шаблонный тег (создаем экземпляр класса Library)
register = template.Library()


# функция-тег (декоратор) для получения категории товаров в html-документах
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


# takes_context=True - значит все контекстные переменные, будут доступны через параметр context
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    # формируем словарь из значений поля request из переменной context
    query = context['request'].GET.dict()
    # теперь нам нужно его расширить каким-нибудь kwargs, тем, что нужно передать из нашего шаблона сюда
    query.update(kwargs)
    # формируем из словаря ключ-значение (возвращает готовую строку, которую можно использовать в url-адресе)
    return urlencode(query)

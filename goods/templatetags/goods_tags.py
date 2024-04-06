# импортируем template
from django import template

# импортируем модель категорий товаров
from goods.models import Categories

# регистрируем шаблонный тег
register = template.Library()


# функция-тег для получения категории товаров в html-документах
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

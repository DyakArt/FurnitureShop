from django import template

from carts.models import Cart

# создаем декоратор для регистрации
register = template.Library()


# декорируем нашу функцию
@register.simple_tag()
def user_carts(request):
    # Проверяем, авторизован ли пользователь
    if request.user.is_authenticated:
        # возвращаем все корзины пользователя
        return Cart.objects.filter(user=request.user)
    else:
        # Возвращаем пустой QuerySet для анонимного пользователя
        return Cart.objects.none()

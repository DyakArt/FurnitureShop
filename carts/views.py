from django.shortcuts import render

from goods.models import Products
from carts.models import Cart

from django.shortcuts import redirect


def cart_add(request, product_slug):
    # получаем экземпляр продукта по слагу, который нужно добавить в корзину
    product = Products.objects.get(slug=product_slug)

    # если пользователь авторизован
    if request.user.is_authenticated:
        # запрашиваем все его корзины, которые есть по конкретному продукту
        carts = Cart.objects.filter(user=request.user, product=product)

        # если у пользователя уже есть этот товар в корзине
        if carts.exists():
            # берём этот товар
            cart = carts.first()
            if cart:
                # добавляем количество на единицу
                cart.quantity += 1
                # сохраняем корзину
                cart.save()
        else:
            # если нет товара в корзине, то создаем его и указываем количество = 1
            Cart.objects.create(user=request.user, product=product, quantity=1)
    # делаем редирект на страницу, на которой был пользователь.
    # В атрибуте META есть ключ HTTP_REFERER, который отвечает за то, с какой страницы мы сюда попали
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    ...


def cart_remove(request, product_slug):
    ...

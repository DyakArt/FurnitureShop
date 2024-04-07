from django.shortcuts import render
# импортируем модель товаров
from goods.models import Products


# отображение каталога
def catalog(request, category_slug):
    # делаем проверку на значение slug
    if category_slug == 'all':
        # получаем все товары из таблицы product
        goods = Products.objects.all()
    else:
        # получаем товары только нужной категории, category - поле внешнего ключа на таблицу Categories
        goods = Products.objects.filter(category__slug=category_slug)
        # если после запроса не нашлось товаров в данной категории
        if not goods.exists():
            goods = False

    context = {
        'title': 'Home - Каталог',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)


# отображение товара, под каждый конвертер из url свой параметр
def product(request, product_slug):
    # получаем товар из БД по slug товара, который получили из ссылки
    prod = Products.objects.get(slug=product_slug)

    # создаем контекст для товара (он будет доступен в html-документе) по имени product
    context = {
        'title': f'Home - {prod.name}',
        'product': prod
    }

    return render(request, 'goods/product.html', context)

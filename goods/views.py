from django.shortcuts import render
# импортируем модель товаров
from goods.models import Products


# отображение каталога
def catalog(request):
    # получаем все товары из таблицы product
    goods = Products.objects.all()

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

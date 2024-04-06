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


# отображение товара
def product(request):
    return render(request, 'goods/product.html')

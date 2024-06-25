from django.shortcuts import render
# импортируем класс для пагинации страниц
from django.core.paginator import Paginator
# импортируем модель товаров
from goods.models import Products


# отображение каталога
def catalog(request, category_slug):
    # получаем номер страницы из объекта request по ключу 'page', если ключа не будет, то открываем 1-ю страницу
    page = request.GET.get('page', 1)
    # делаем проверку на значение slug
    if category_slug == 'all':
        # получаем все товары из таблицы product
        goods = Products.objects.all()
    else:
        # получаем товары только нужной категории, category - поле внешнего ключа на таблицу Categories
        goods = Products.objects.filter(category__slug=category_slug)
    # если после запроса не нашлось товаров в данной категории
    if not goods.exists():
        current_page = False
    else:
        # создаем переменную paginator
        # goods - имя queryset (имя переменной, в которой происходит запрос объектов)
        # par_page - сколько объектов выводить на каждой странице (3 товара)
        paginator = Paginator(goods, 3)

        # переменная для страницы, которая будет отображаться пользователю
        # в метод page передаем нужную страницу для отображения (1 - первая страница)
        current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug
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

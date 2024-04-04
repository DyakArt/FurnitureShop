from django.shortcuts import render


# отображение каталога
def catalog(request):
    return render(request, 'goods/catalog.html')


# отображение товара
def product(request):
    return render(request, 'goods/product.html')

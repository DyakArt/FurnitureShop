from django.urls import path

from goods import views

# необходимо указать имя приложения для пространства имён (namespace), чтобы не было ошибки
app_name = 'goods'

# первый аргумент в path - это адрес конкретной страницы,
# второй аргумент - регистрация представления, которое будет закреплено за этим адресом
# третий аргумент - для тегов в html-документах, чтобы можно было обращаться к этим ссылкам по имени
urlpatterns = [
    path('search/', views.catalog, name='search'),
    # путь для страницы с каталогом товаров
    # <slug:category_slug>/ - конвертер url-адреса для каждой категории, category_slug - параметр в функции catalog
    path('<slug:category_slug>/', views.catalog, name='index'),
    # путь для страницы конкректного товара
    # <slug:product_slug>/ - конвертер url-адреса для каждого товара, product_slug - параметр в функции product
    path('product/<slug:product_slug>/', views.product, name='product'),
]


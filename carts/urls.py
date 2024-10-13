from django.urls import path

from carts import views

# необходимо указать имя приложения для пространства имён (namespace), чтобы не было ошибки
app_name = 'carts'

# первый аргумент в path - это адрес конкретной страницы,
# второй аргумент - регистрация представления, которое будет закреплено за этим адресом
# третий аргумент - для тегов в html-документах, чтобы можно было обращаться к этим ссылкам по имени
urlpatterns = [
    # путь для добавления в корзину
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    # путь для изменения содержимого в корзине
    path('cart_change/<int:product_id>/', views.cart_change, name='cart_change'),
    # путь для удаления из корзины
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]


"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# импортируем setting.py из приложения app
from django.conf import settings

# импортируем функцию static для медиа-файлов
from django.conf.urls.static import static

# первый аргумент в path - это адрес конкретной страницы,
# второй аргумент - регистрация представления, которое будет закреплено за этим адресом
# третий аргумент - для тегов в html-документах, чтобы можно было обращаться к этим ссылкам по имени
urlpatterns = [
    path('admin/', admin.site.urls),
    # подключаем адреса для приложения main (главная страница, о нас)
    # namespace - имя приложения, к которому относятся url-адреса, когда мы обращаемся к ним в html-шаблонах templates
    path('', include('main.urls', namespace='main')),
    # подключаем адреса для приложения goods (каталог товаров, товары)
    path('catalog/', include('goods.urls', namespace='catalog')),
    # подключаем адреса для приложения users
    path('user/', include('users.urls', namespace='user')),
    # подключаем адреса для приложения carts
    path('cart/', include('carts.urls', namespace='cart'))
]

# при отладке (debug = true), будем подключать дополнительный инструмент для более детальной отладки
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

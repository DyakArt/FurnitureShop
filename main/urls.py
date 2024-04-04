from django.urls import path

from main import views

# необходимо указать имя приложения для пространства имён (namespace), чтобы не было ошибки
app_name = 'main'

# первый аргумент в path - это адрес конкретной страницы,
# второй аргумент - регистрация представления, которое будет закреплено за этим адресом
# третий аргумент - для тегов в html-документах, чтобы можно было обращаться к этим ссылкам по имени
urlpatterns = [
    # путь для главной страницы
    path('', views.index, name='index'),
    # путь для страницы о нас
    path('about/', views.about, name='about'),
]
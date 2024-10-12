from django.urls import path

from users import views

# необходимо указать имя приложения для пространства имён (namespace), чтобы не было ошибки
app_name = 'users'

# первый аргумент в path - это адрес конкретной страницы,
# второй аргумент - регистрация представления, которое будет закреплено за этим адресом
# третий аргумент - для тегов в html-документах, чтобы можно было обращаться к этим ссылкам по имени
urlpatterns = [
    # путь для входа
    path('login', views.login, name='login'),
    # путь для страницы регистрации
    path('registration/', views.registration, name='registration'),
    # путь для страницы профиля
    path('profile/', views.profile, name='profile'),
    # путь для выхода
    path('logout/', views.logout, name='logout'),
]
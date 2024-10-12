from django.db import models
from django.contrib.auth.models import AbstractUser


# Переопределяем модель класса AbstractUser
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')

    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'user'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Пользователя'
        # в множественном числе
        verbose_name_plural = 'Пользователи'

    # метод перегрузки для вывода объекта (изменяем отображение каждого пользователя в админ панели)
    def __str__(self):
        return self.username

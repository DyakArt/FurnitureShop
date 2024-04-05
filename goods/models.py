from django.db import models


# Через эти классы мы также можем взаимодействовать с таблицами из БД.
# Создаем таблицу для категорий товаров
class Categories(models.Model):
    # перечисляем поля (атрибуты) таблицы
    # название категории товаров (имя каждой категории должно быть уникальным)
    # verbose_name - название поля в админ панели
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    # фрагмент url-адреса, который будет вести на соответствующую категорию товаров (тоже уникальный),
    # может быть пустой (blank=True и null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    # создаем класс, чтобы поменять некоторые данные (например, название таблицы в БД, в админ панели)
    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'category'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Категорию'
        # в множественном числе
        verbose_name_plural = 'Категории'

    # метод перегрузки для вывода объекта (изменяем отображение имени каждой категории в админ панели)
    def __str__(self):
        return self.name


# Создаем таблицу для информации о товарах
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    # TextField - тип для больших текстов, хорошо подойдёт для описания товара
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    # upload_to - где хранить изображение (ссылка)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    # DecimalField - тип для чисел с плавающей точкой
    # default - дефолтное значение (допустим, когда товар закончился)
    # max_digits - максимальное количество цифр
    # decimal_places - максимальное количество цифр после запятой (будет округляться)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    # количество товара (PositiveIntegerField - не может содержать отрицательные значения)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    # получаем (связываем) таблицу Categories (внешний ключ)
    # to - к какой таблице привязываем внешний ключ
    # on_delete - что делать, при удалении какой-то категории, которая была привязана к товарам.
    # PROTECT - запрет на удаление категории, пока с ней связаны какие-то товары.
    # CASCADE - при удалении категории, удалятся и все товары, связанные с ней.
    # SET_DEFAULT - при удалении категории, все товары, что были связаны с ней будут привязаны к
    # новой дефолтной категории.
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        # обычно таблицы называют в единственном числе (здесь, как она будет отображаться в БД)
        db_table = 'product'
        # как будет отображаться в админ панели (в единственном числе)
        verbose_name = 'Продукт'
        # в множественном числе
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

from django.contrib import admin
# чтобы таблица отображалась в админ панели, нужно зарегистрировать её здесь

# импортируем таблицу Categories
from goods.models import Categories, Products

# регистрируем таблицу Categories в админ панели
# admin.site.register(Categories)
# регистрируем таблицу Products в админ панели
# admin.site.register(Products)


# определяем класс для тонкой настройки Categories в админ панели
# и декорируем его (выполняем регистрацию Categories в админ панели)
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # определяем какие поля будут заполняться автоматически
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # определяем какие поля будут заполняться автоматически
    prepopulated_fields = {
        'slug': ('name',)
    }

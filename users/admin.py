from django.contrib import admin
from users.models import User

# регистрируем таблицу User в админ панели
admin.site.register(User)

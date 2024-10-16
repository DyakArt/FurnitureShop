from django.db import models

from users.models import User
from goods.models import Products


# переопределим QuerySet, который будет обслуживать модель Cart и её объекты (корзины)
class CartQuerySet(models.QuerySet):
    #
    def total_price(self):
        # перебираем каждый объект (корзину), сначала рассчитываем стоимость каждой корзины (товар + количество),
        # а потом стоимость всех корзин через метод sum - это будет общая сумма к оплате
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        # если есть какой-нибудь объект (корзина)
        if self:
            # считаем количество в каждой корзине, потом суммируем количество всех корзин и возвращаем
            return sum(cart.quantity for cart in self)
        # иначе возвращаем 0 объектов (корзин)
        return 0


# на каждый товар, который пользователь добавляет, собирается купить, мы создаем отдельную корзину (запись)
# связывая с пользователем, и там хранится только один продукт и его количество
# получается, что наша виртуальная корзина состоит из множества корзин (записей) в нашей БД
# это удобно, так как потом легче делать аналитику по корзинам и заказанным товарам по БД
# также намного проще писать запросы
class Cart(models.Model):
    # делаем внешний ключ на модель User, каскадная модель
    # прописываем blank, null = True, если пользователя нет (не зарегистрирован), то поле может быть пустым
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    # делаем внешний ключ на модель Product, каскадная модель
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    # добавляем ключ сессии.
    # если пользователь не авторизован, то будем вносить информацию о товарах не по пользователю (User модель),
    # а по ключу сессии, а при попытке оформить заказ будет просьба авторизоваться, затем пользователя перекидывает
    # на страницу авторизации, он вводит данные, и тогда мы перекинем его привязку с сессионного ключа на модель User
    session_key = models.CharField(max_length=32, null=True, blank=True)
    # поле, которое хранит дату, auto_now_add - как только пользователь добавит товар в корзину,
    # там будет указываться дата создания этой корзины
    # по этому полю можно делать напоминание, или чтобы старые корзины через какое-то время удалялись
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    # определяем цену товара, учитывая его количество
    def products_price(self):
        # перемножаем итоговую цену на количество товара
        # округляем до двух знаков после запятой
        return round(self.product.sell_price() * self.quantity, 2)

    #
    objects = CartQuerySet().as_manager()

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзину'
        verbose_name_plural = 'Корзины'

    # чтобы менеджерам было удобно смотреть какие у пользователя есть товары и их количество
    def __str__(self):
        return f'Корзина пользователя: {self.user.username} | Название товара: {self.product.name} | Количество: {self.quantity}'

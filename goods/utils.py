from django.db.models import Q

from goods.models import Products


def q_search(query):
    # поиск по id товара
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # перебираем все слова в поиске, заносим в список только те, которые больше 2
    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    # |= работает как +=
    # все слова с помощью этой конструкции пойдут в один большой запрос
    # поиск и по описанию и по названию
    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)

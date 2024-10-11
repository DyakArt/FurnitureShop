from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

from goods.models import Products


def q_search(query):
    # поиск по id товара
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # Полнотекстовый поиск от Django (использует похожие токены и вероятность, чтобы находить слова из поиска, падежи,
    # буква ё и тд)
    # определяем вектор, который работает по двум полям для поиска
    vector = SearchVector("name", "description")
    # передаем наш запрос из поля поиска
    query = SearchQuery(query)
    # возвращаем нужный queryset, а при помощи класса SearchRank, мы добавляем к каждому объекту поле rank,
    # которое рассчитывает как сильно совпадает информация в товаре или в статье с введенным поисковым запросом,
    # сортируем от более подходящего к менее подходящему
    # добавляем фильтр для исключения товаров с нулевым рангом, чтобы отображались нужные товары (с рангом больше 0)
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    # делаем отдельный стиль для названия товара
    # по названию товара ищем слова из запроса и выделяем нужным цветом с помощью тега span
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    # делаем отдельный стиль для описания товара
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    # возвращаем результат поиска
    return result

    # # полнотекстовый поиск
    # # перебираем все слова в поиске, заносим в список только те, которые больше 2
    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    #
    # # |= работает как +=
    # # все слова с помощью этой конструкции пойдут в один большой запрос
    # # поиск и по описанию и по названию
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Products.objects.filter(q_objects)

from math import sqrt

# оригинальный словарь
critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'You, Me and Dupree': 2.5
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0
    }
}


# возвращаем оценку подобия person1 и person2 на основе расстояния
def sim_distance(prefs, person1, person2):
    # получаем список предметов, оцененных обоими
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    # если нет ни одной общей оценки, вернем 0
    if len(si) == 0:
        return 0
    # сложим квадраты разностей
    sum_of_squares = sum(
        [pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sum_of_squares)


# возвращает коэффициент корреляции Пирсона между p1 и p2
def sim_person(prefs, p1, p2):
    # получаем список объектов, оцененных обоими
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1
    # найти число элементов
    n = len(si)
    # если нету ни одной общей оценки, вернуть 0
    if n == 0:
        return n
    # вычисляем сумму всех предпочтений
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # вычисляем сумму квадратов
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # вычисляем сумму произведений
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # вычисляем коэффициент корреляции Пирсона
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return den
    r = num / den
    return r


# возвращает список наилучших соответствий для человека из словаря prefs
# Количество результатов в списке и функция подобия - необязат. параметры
def topMatches(prefs, person, n=5, similarity=sim_person):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    # отсортировать список по убыванию оценок
    scores.sort()
    scores.reverse()
    return scores[0:n]


# получить рекомендации для заданного человека, пользуясь взвешенным средним оценок,
# данных всеми остальными пользователями
def getRecommendations(prefs, person, similarity=sim_person, limit=5):
    totals = {}
    simSums = {}
    for other in prefs:
        # сравнивать меня с собой не нужно
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # игнорировать нулевые и отрицательные оценки
        if sim <= 0:
            continue
        for item in prefs[other]:
            # оцениваем только фильмы, которые мы еще не смотрели
            if item not in prefs[person] or prefs[person][item] == 0:
                # коэффициент подобия * оценка
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # сумма коэффициента подобия
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # создаем нормализованный список
    rankings = [(total / simSums[item], item) for item, total in totals.items()]
    # возвращаем отсортированный список
    rankings.sort()
    rankings.reverse()
    return rankings[0:limit]


# преобразование словаря
def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # меняем местами человека и предмет
            result[item][person] = prefs[person][item]
    return result

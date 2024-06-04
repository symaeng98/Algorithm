def solution(cacheSize, cities):
    cache = []
    result = 0
    for city_up in cities:
        city = city_up.lower()
        if city not in cache:
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                result += 5
            else:
                result += 5
        else:
            cache.remove(city)
            cache.append(city)
            result += 1

    return result
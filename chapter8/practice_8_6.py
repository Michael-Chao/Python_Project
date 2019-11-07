def city_country(city, country):
    relation = [city.title() + " , " + country.title()]
    return relation
relation = city_country('xian', 'china')
print(relation)
relation = city_country('beijing', 'china')
print(relation)
relation = city_country('xiping', 'china')
print(relation)
def describe_city(city='Reykjavik', country='Iceland'):
    """城市名字以及所属国家"""
    print(city.title() + " is in " + country.title() + ".")

describe_city()
describe_city('xian', 'china')
describe_city(country='china')
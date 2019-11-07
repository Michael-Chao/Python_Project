cities = {
    'Beijing': {
        'country': 'china',
        'population': '14b',
        'fact': 'history'
        },
    'New York': {
        'country': 'america',
        'population': '3b',
        'fact': 'wealth'
        },
    'xiping': {
        'country': 'china',
        'population': '0.5b',
        'fact': 'home'
        },
    }
for name, name_info in cities.items():
    print("\nCity: " + name.title())
    print("Information: " + name_info['country'] + "\n\t\t\t" + name_info['population'] + "\n\t\t\t" + name_info['fact'])
favorite_places = {
    'Chao Xu': ['Xi Ping', 'Beijing', 'Chongqing'],
    'Xiao Ming': ['wuhan', 'nanjing', 'chengdu'],
    'Liu Liu': ['haerbin', 'changchun', 'bujidao'],
    }
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place)
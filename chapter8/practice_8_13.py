def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for v, k in user_info.items():
        profile[v] = k
    return profile

user_profile = build_profile('Xu', 'Chao', location= 'xiping', field = 'computer', age = 23)
print(user_profile)
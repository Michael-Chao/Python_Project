def cars_info(manufacturer, model, **introduction):
    """将汽车的信息存储在字典中"""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for k, v in introduction.items():
        profile[k] = v
    return profile

introduction = cars_info('japan', 'toyoto', color = 'red', tow_package = True)
print(introduction)
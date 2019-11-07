def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含一个人的信息"""
    if age:
        person = {"first": first_name, "last": last_name, 'age': age}
    else:
        person = {"first": first_name, "last": last_name}
    return  person
musician = build_person('jesica', 'chou', 9)
print(musician)
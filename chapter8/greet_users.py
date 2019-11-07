def greet_users(names):
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        print("Hello, " + name.title() + "!")
names = ['lili', 'harry', 'james']
greet_users(names)
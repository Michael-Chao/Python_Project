voted = {}

def check_voter(name):
    """检测是否投票"""
    if voted.get():
        print("kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")
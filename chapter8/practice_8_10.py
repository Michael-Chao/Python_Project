def make_great(unmodificated_members, modificated_members):
    """给每个魔术师名字中都添加'the Great'"""
    for maginician in unmodificated_members:
        current_magician = "the Great " + maginician
        modificated_members.append(current_magician)

def show_magicians(modificated_members):
    """打印魔术师名字"""
    print("\n")
    for maginician in modificated_members:
        print(maginician.title())

unmodificated_members = ['david', 'lili', 'harry']
modificated_members = []

make_great(unmodificated_members[:], modificated_members)
show_magicians(modificated_members)
show_magicians(unmodificated_members)
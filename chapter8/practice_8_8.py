def make_allbum(name, album):
    """描述音乐专辑"""
    current_album = {'name': name, 'album': album}
    return current_album
while True:
    print("\nPlease enter the singer's name. ")
    print("(enter 'q' when you finished)")
    name = input("Singer name:")
    if name == 'q':
        break

    album = input("The album: ")
    if album == 'q':
        break

    last_list = make_allbum(name, album)
    print(last_list)

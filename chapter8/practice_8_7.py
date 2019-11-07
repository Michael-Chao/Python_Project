def make_allbum(name, album, number=''):
    """描述音乐专辑"""
    if number:
        current_album = {'name': name, 'album': album, 'number': number}
    else:
        current_album = {'name': name, 'album': album}
    return current_album
first_album = make_allbum('jay chou', '青花瓷', 9)
print(first_album)
second_album = make_allbum('jay chou', '告白气球')
print(second_album)
third_album = make_allbum('jj', '江南', 6)
print(third_album)

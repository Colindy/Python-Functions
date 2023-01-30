# A dictionary with some album information

def make_album(artist, album, songs = None):
    music = {'Artist Name': artist, 'Album Title': album}
    if songs:
        music['No of Songs'] = songs
    return music

info1 = make_album('Metallica', 'S&M Album')
print(info1)
info2 = make_album('Nirvana', 'Nevermind')
print(info2)
info3 = make_album('Disturbed', 'The Sickness')
print(info3)
info4 = make_album('RHCP', 'Californication', '15')
print(info4)
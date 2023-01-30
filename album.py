# A dictionary with some album information

# First my function
def make_album(artist, album, songs = None):
    music = {'Artist Name': artist, 'Album Title': album}
    if songs:
        music['No of Songs'] = songs
    return music

# Now a couple of calls with some info and printing to show the output
info1 = make_album('Metallica', 'S&M Album')
print(info1)
info2 = make_album('Nirvana', 'Nevermind')
print(info2)
info3 = make_album('Disturbed', 'The Sickness')
print(info3)
info4 = make_album('RHCP', 'Californication', '15')
print(info4)

# Now going to get user input and create from that
while True:
    print("Going to get some artist info from you now.")
    print("(Type 'q' if you want to quit at any time)")
    inartist = input("What's your favorite artist? ")
    if inartist == 'q':
        break
    inalbum = input("And your favorite Album by said artist? ")
    if inalbum == 'q':
        break
    insongs = input("How many songs on that album? ")
    if insongs == 'q':
        break
    ininfo = make_album(inartist, inalbum, insongs)
    print(ininfo)
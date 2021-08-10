import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

album1 = Album('Pulse', 'Pop', artist1)
album_repository.save(album1)

album2 = Album('Thriller', 'Rhythm and blues', artist2)
album_repository.save(album2)

artist1 = Artist('Toni Braxton')
album_repository.save(artist1)

artist2 = Artist('Michael Jackson')
album_repository.save(artist1)



for album in album_repository.select_all():
    print(album.__dict__)



pdb.set_trace()

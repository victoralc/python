from oo.movies.Playlist import Playlist


class Media:
    def __init__(self, name, year):
        self._name = name.title()
        self._year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Movie(Media):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return "[Name: {}, Year: {}, Duration: {} min, Likes: {}]"\
            .format(self._name, self._year, self._duration, self._likes)


class Series(Media):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons

    @property
    def seasons(self):
        return self._seasons

    def __str__(self):
        return "[Name: {}, Year: {}, Seasons: {}, Likes:{}]"\
            .format(self._name, self._year, self._seasons, self._likes)


avengers = Movie("Avengers", 2018, 160)
avengers.like()
avengers.name = "Avengers Infinity War"

lord_of_the_rings = Movie("Lord of the Rings", 2001, 240)
lord_of_the_rings.like()
lord_of_the_rings.like()
lord_of_the_rings.like()
lord_of_the_rings.like()

sherlock = Series("Sherlock", 2017, 5)
sherlock.like()
sherlock.like()

the_witcher = Series("The Witcher", 2018, 5)

movies_and_series = [avengers, sherlock, lord_of_the_rings, the_witcher]

weekend_playlist = Playlist('My weekend playlist', movies_and_series)

print(f'Has program?:  {sherlock in weekend_playlist}')
print(f'Size of my playlits:  {len(weekend_playlist)}')
print(f'Item in 3 position:  {weekend_playlist[3]}')

for tv_program in weekend_playlist:
    print(tv_program)

print("Film library")


class Films:
    def __init__(self, name, year, genre):
        self.name = name
        self.year = year
        self.genre = genre
        self.current_views = 0

    def play(self, step=1):
        print(self.current_views + step)

    def watch(self):
        print(f"{self.name} ({self.year})")


film_1 = Films(name="A Space Odyssey", year="1968", genre="science fiction")
film_2 = Films(name="The Godfather", year="1972", genre="thriller")
film_3 = Films(name="Citizen Kane", year="1941", genre="drama")
film_4 = Films(name="La Dolce Vita", year="1960", genre="drama")
film_5 = Films(name="Seven Samurai", year="1954", genre="action")


class Series:
    def __init__(self, name, year, genre, episode, season):
        self.name = name
        self.year = year
        self.genre = genre
        self.episode = episode
        self.season = season
        self.current_views = 0

    def watching(self):
        print(f"{self.name} S0{self.season}E0{self.episode}")

    def play(self, step=1):
        print(self.current_views + step)


serial_1 = Series(name="The Handmaid's Tale", year="2017", genre="biography", episode="1", season=1)
serial_2 = Series(name="Fringe", year="2008", genre="science fiction", episode="4", season=2)
serial_3 = Series(name="Scrubs", year="2001", genre="drama", episode="7", season=3)
serial_4 = Series(name="Supernatural", year="2005", genre="science fiction", episode="3", season=1)
serial_5 = Series(name="Bosch", year="2014", genre="drama", episode="9", season=2)
pass

# creating lists, have few experiments =)
library_1 = [Films, Series]
library_2 = [serial_1.name, serial_2.name, serial_3.name, serial_4.name, serial_5.name, film_1.name, film_2.name, film_3.name, film_4.name, film_5.name]
library_3 = [serial_1, serial_2, serial_3, serial_4, serial_5, film_1, film_2, film_3, film_4, film_5]


# just for testing
serial_2.watching()
serial_2.play()
film_3.watch()

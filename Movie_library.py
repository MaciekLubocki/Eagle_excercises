import random
import operator

class Movie():
  instances = []
  def __init__(self, title, release_date, genre, display_counter):
       self.title = title
       self.release_date = release_date
       self.genre = genre
       self.display_counter = display_counter
       __class__.instances.append(self)

 
  def play(self):
       self.display_counter += display_counter + 1 
       return display_counter   

  def __str__(self):
       return f'{self.title} {self.release_date}'

    
class Serial(Movie):
  instances = []
  def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
        __class__.instances.append(self)
        
  def __str__(self):
        return f'{self.title} S{self.season_number}E{self.episode_number}'


pulp_fiction = Movie(title="Pulp Fiction", release_date = "1998", genre="fantasy", display_counter="10" )
never_ending_story = Movie(title="Never Ending Story", release_date = "1989", genre="fantasy", display_counter="4")
charisma = Movie(title="Charisma", release_date = "2002", genre="drama", display_counter="15")
godzilla = Movie(title="Godzilla", release_date = "2012", genre="comedy", display_counter="20")
jurassic_park = Movie( title="Jurassic Park", release_date = "1994", genre="documentary", display_counter="18")
simpsons_1s1e = Serial(title="The Simpsons", release_date = "1985", genre="comedy", episode_number ="01", season_number="01", display_counter="30")
simpsons_1s2e = Serial(title="The Simpsons", release_date = "1985", genre="comedy", episode_number ="01", season_number="02", display_counter="15")
simpsons_1s3e = Serial(title="The Simpsons", release_date = "1985", genre="comedy", episode_number ="01", season_number="03", display_counter="50")
simpsons_1s4e = Serial(title="The Simpsons", release_date = "1986", genre="comedy", episode_number ="01", season_number="04", display_counter="10")
simpsons_1s5e = Serial(title="The Simpsons", release_date = "1986", genre="comedy", episode_number ="01", season_number="05", display_counter="52")


library_collection = [pulp_fiction, never_ending_story, charisma, godzilla, jurassic_park, simpsons_1s1e, simpsons_1s2e,
                    simpsons_1s3e, simpsons_1s4e, simpsons_1s5e ]


def get_movies(): 
  only_movies = [movie for movie in library_collection if type(movie) == Movie]
  movies_sorted_title = sorted(only_movies, key=lambda only_movies: only_movies.title)
  print(*movies_sorted_title, sep ="\n")
get_movies()

def get_series(): 
  only_series = [series for series in library_collection if type(series) == Serial]
  series_sorted_title = sorted(only_series, key=lambda only_series: only_series.title)
  print(*series_sorted_title, sep ="\n")
get_series()


def movie_search():
  search = input("Wprowadź nazwę filmu lub serialu, który szukasz: ")
  for movie in library_collection:
      if movie.title == search:
        print(movie)
movie_search()

def generate_views():
      random_view = random.choices(library_collection, k=1)
      random_number=random.randint(1, 100)
      display_counter = int(random_view[0].display_counter) + random_number
      print ("Losowo wybrany obiekt z kolekcji: ", random_view[0].title,",", "Ilość wyświetleń: ", display_counter)
generate_views()    


def generate_views_multiple():
  [generate_views() for _ in range(9)]
generate_views_multiple()


def top_titles(): 
  choose_type = input("Wybierz poprzez numer jakiej kategorii najpopularniejsze filmy chcesz zobaczyć: 1. Filmy 2. Seriale 3. Wszystkie produkcje: ")
  if int(choose_type) == 1:
      only_movies = [movie for movie in library_collection if type(movie) == Movie]
      item_output = sorted(only_movies, key=lambda only_movies: only_movies.display_counter)
  elif int(choose_type) == 2:
      only_series = [series for series in library_collection if type(series) == Serial]
      item_output = sorted(only_series, key=lambda only_series: only_series.display_counter)
  else:
      item_output = sorted(library_collection, key=operator.attrgetter('display_counter'))
  print(*item_output, sep ="\n")
top_titles()


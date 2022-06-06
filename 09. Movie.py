class Movie:
    __watched_movies = 0
    __movies = list()

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if self.name not in Movie.__movies:
            Movie.__movies.append(self.name)
            Movie.__watched_movies += 1
            self.watched = True

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
first_movie.watch()
third_movie.watch()
third_movie.change_name("My Movie")
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
print(Movie.renamed)

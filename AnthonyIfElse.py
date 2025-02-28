
movie_count = 15  # number of movies I saw last year
arbitrary_number = 10  # an arbitrary number

if movie_count > arbitrary_number:
    print("You watched a lot of movies!")
else:
    print("You watched few movies...")

avg_movies_watched = (20 + 6 + 8 + 11 + 0 + movie_count) / 6

print("average movies watched:", avg_movies_watched)

if movie_count > avg_movies_watched:
    print("You watched more movies than the (mean) average.")
elif movie_count == avg_movies_watched:
    print("You watched the same # of movies as the average.")
else:
    print("You watched less movies than the (mean) average.")
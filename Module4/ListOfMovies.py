# 1. Create a list of your favorite movies and print the third movie in the list.
movies = ["Rab ne bana Di Jodi ", "Jawan " , "Chhava ","Pk" , "Zindagi na milegi dobara"]
print(movies[2])
# 2. Add a new movie to the list and print the updated list.
movies.append("Animal")
print(movies)

# 3. Remove the second movie from the list and print the updated list.

movies.remove(movies[1])
print(movies)

# 4. Sort the list in alphabetical order and print the sorted list.
movies.sort()
print(movies)

newMovies = []
newMovies.append(movies[0])
newMovies.append(movies[len(movies)-1])
print(newMovies)
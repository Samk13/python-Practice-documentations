remainders = [x**2 % 5 for x in range(1, 220)]

print(remainders)

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Gone with the Wind", "Annie Hall", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill a Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Spirited Away", "Groundhog Day", "Like Stars on Earth", "Sunset Blvd.", "Scent of a" ]

gMovies = [title for title in movies if title.startswith("G")]
# for title in movies:
#     if title.startswith("G"):
#         gMovies.append(title)

print(gMovies)

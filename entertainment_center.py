import media
import fresh_tomatoes

trinity = media.Movie(
    "Trinity is still my name",
    "Terence Hill and Bud Spencer in Trinity",
    "https://goo.gl/sEjmoH",
    "https://www.youtube.com/watch?v=pRwKywm7qh4",
    1971
)

starwars = media.Movie(
    "Star Wars",
    "A movie about Luke Skywalker",
    "https://goo.gl/miM1QG",
    "https://www.youtube.com/watch?v=1g3_CFmnU7k",
    1977
)

braveheart = media.Movie(
    "BraveHeart",
    "A movie about William Wallace",
    "https://goo.gl/Sm5mPE",
    "https://www.youtube.com/watch?v=wj0I8xVTV18",
    1995
)

thegood_thebad_theugly = media.Movie(
    "The Good, The Bad and The Ugly",
    "",
    "https://goo.gl/ShihNW",
    "https://www.youtube.com/watch?v=D5PpsKZFvPU",
    1968
)

tombstone = media.Movie(
    "Tombstone",
    "",
    "https://goo.gl/WjBPUY",
    "https://www.youtube.com/watch?v=XTWYKf5hXIg",
    1993
)

back_to_the_future = media.Movie(
    "Back to the Future",
    "",
    "https://goo.gl/xP1TuD",
    "https://www.youtube.com/watch?v=2LnShmQ_hLc",
    1985
)

movies = [trinity, starwars, braveheart, thegood_thebad_theugly, 
          tombstone, back_to_the_future]

fresh_tomatoes.open_movies_page(movies)

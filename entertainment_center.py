import media
import fresh_tomatoes

# Instances of movies for the web site
trinity = media.Movie(
    "Trinity is still my name",
    "Bambino tries to teach his brother Trinity how to become an outlaw,"
    " but the two wind up saving a pioneer family and breaking up an arms"
    " ring instead.",
    "https://i.imgur.com/GyBR4U3.jpg",
    "https://www.youtube.com/watch?v=pRwKywm7qh4",
    1971
)

starwars = media.Movie(
    "Star Wars",
    "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot"
    ", a Wookiee and two droids to save the galaxy from the Empire's"
    " world-destroying battle-station while also attempting to rescue"
    " Princess Leia from the evil Darth Vader.",
    "https://i.imgur.com/AJEEZXe.jpg",
    "https://www.youtube.com/watch?v=1g3_CFmnU7k",
    1977
)

braveheart = media.Movie(
    "BraveHeart",
    "When his secret bride is executed for assaulting an English"
    " soldier who tried to rape her, Sir William Wallace begins a"
    " revolt against King Edward I of England.",
    "https://i.imgur.com/W0wYg17.jpg",
    "https://www.youtube.com/watch?v=wj0I8xVTV18",
    1995
)

thegood_thebad_theugly = media.Movie(
    "The Good, The Bad and The Ugly",
    "A bounty hunting scam joins two men in an uneasy alliance"
    " against a third in a race to find a fortune in gold buried"
    " in a remote cemetery.",
    "https://i.imgur.com/R1c9Buz.jpg",
    "https://www.youtube.com/watch?v=D5PpsKZFvPU",
    1968
)

tombstone = media.Movie(
    "Tombstone",
    "A successful lawman's plans to retire anonymously in Tombstone,"
    " Arizona, are disrupted by the kind of outlaws he was famous for"
    " eliminating.",
    "https://i.imgur.com/eothbuo.jpg",
    "https://www.youtube.com/watch?v=XTWYKf5hXIg",
    1993
)

back_to_the_future = media.Movie(
    "Back to the Future",
    "Marty McFly, a 17-year-old high school student,"
    " is accidentally sent thirty years into the past"
    " in a time-traveling DeLorean invented by his close friend,"
    " the maverick scientist Doc Brown.",
    "https://i.imgur.com/Lro71la.jpg",
    "https://www.youtube.com/watch?v=2LnShmQ_hLc",
    1985
)

# List of movies to render in the web site
movies = [trinity, starwars, braveheart, thegood_thebad_theugly, tombstone, back_to_the_future]

# Call fresh_tomatoes function that generates the html page and call the web browser
fresh_tomatoes.open_movies_page(movies)

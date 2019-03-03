import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story 4",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=P9-jf9-c9JM")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=WbMD53XPJWA")

three_idiots = media.Movie("3 idiots",
                           "A story of three Engineering students.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w")


dangal = media.Movie("Dangal",
                     "Story of two indian woman wrestelrs from Haryana and their struggle.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Dangal_Poster.jpg/220px-Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

fate_of_furious = media.Movie("The Fate of the Furious",
                              "Story of Racers with a lot of actions.",
                              "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                              "https://www.youtube.com/watch?v=uisBaTkQAEs")

chak_de_india = media.Movie("Chak de India",
                            "A story of Indian women Hockey team.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Chak_De%21_India.jpg/220px-Chak_De%21_India.jpg",
                            "https://www.youtube.com/watch?v=6a0-dSMWm5g")

movies = [toy_story, avatar, three_idiots,
          dangal, fate_of_furious, chak_de_india]

# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)
# print(media.Movie.__bases__)
# print(media.Movie.__dict__)

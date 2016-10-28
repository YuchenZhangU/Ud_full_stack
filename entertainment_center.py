import media
import fresh_tomatoes

infernal_affairs3 = media.Movie("Infernal Affairs 3", 
                                "A story about hongkong police and gangsterdom",
                                "https://upload.wikimedia.org/wikipedia/en/6/6d/Infernal_Affairs_3.jpg",
                                "https://www.youtube.com/watch?v=9EjS2fk2bb4")

infernal_affairs2 = media.Movie("Infernal Affairs 2", 
                                "A story about hongkong police and gangsterdom",
                                "https://upload.wikimedia.org/wikipedia/en/5/5a/Infernal_Affairs_II.jpg",
                                "https://www.youtube.com/watch?v=TaDUZskpMfM")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                "A story about korea socity",
                                "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                "https://www.youtube.com/watch?v=6hB3S9bIaco")

the_terror_live = media.Movie("The Terror Live",
                                "A story about how banker Andy Dufresne escape from jail",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/e/ea/The_Terror%2C_LIVE_poster.jpg/440px-The_Terror%2C_LIVE_poster.jpg",
                                "https://www.youtube.com/watch?v=e_FSvAQMGNc")


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Toy Story",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

movies = [ the_terror_live, infernal_affairs3, infernal_affairs2,the_shawshank_redemption, toy_story, avatar,]
#print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__name__)
print(media.Movie.__module__)
print(__name__)
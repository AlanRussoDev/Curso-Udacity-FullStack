import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a bow and his toy that come to life",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=E8Od9icDijo")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=rZfRsJKoLpc")

euficoloko = media.Movie("Eu fico louco",
                     "A história de um loser que virou fenomeno",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcTdipRj3k1fJ8wrn3Nbkm5bi9NzHvqq7oqiRhR7nZiFe4G-uAzA",
                     "https://www.youtube.com/watch?v=rZfRsJKoLpc")

xxx = media.Movie("xxx",
                     "the history of hitman",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcTZGIMnEFugThYH7TeP21E-AZlvv3-aJEBTKkD0c-dhae7fGTFh",
                     "https://www.youtube.com/watch?v=rZfRsJKoLpc")

theman = media.Movie("The Man Who Fell to Earth",
                     "The Man Who Fell to Earth",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcQjx38iZF0Ysz5APKsAc_j67WDKLXkTMDZmegTAORKdhaw635qW",
                     "https://www.youtube.com/watch?v=rZfRsJKoLpc")

angel = media.Movie("Anjos da Noite: Guerras de Sangue",
                     "the angel",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcRYeU4U0IEM1V81KZ1fZ46ZW6jrBoGg_YZg1P5wYVau780E6Hxa",
                     "https://www.youtube.com/watch?v=rZfRsJKoLpc")





movies = [toy_story,avatar,euficoloko,theman,angel]

fresh_tomatoes.open_movies_page(movies)

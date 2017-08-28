#import file 'media' so that we may reference class Movie and its functions
import media
#import the premade repository that contains html format and the open_movies_page function 
import fresh_tomatoes

#create an instance of  class Movie and add the title, storyline, poster image, and youtube trailer
toy_story = media.Movie("Toy Story",
                                 "Story about toys.",
                                 "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                 "https://www.youtube.com/watch?v=KYz2wyBy3kc")

kisskiss_bangbang = media.Movie("Kiss Kiss, Bang Bang",
                                "All you need to know is that it stars RDJ",
                                "https://upload.wikimedia.org/wikipedia/en/6/61/Kiss_kiss_bang_bang_poster.jpg",
                                "https://www.youtube.com/watch?v=__PnD1HWXSo")

scott_pilgrim = media.Movie("Scott Pilgrim",
                            "A movie about a canadian teenager with a dangerous love triangle. Oh, and everyone apparently has super powers.",
                            "https://upload.wikimedia.org/wikipedia/en/1/14/Scott_Pilgrim_vs._the_World_teaser.jpg",
                            "https://www.youtube.com/watch?v=8NUBVcit5VM")

#create a table that stores all of our instances of Movie
movie = [toy_story, kisskiss_bangbang, scott_pilgrim]
#call our premade repository to use open_movies_page and store our table in the arguments
fresh_tomatoes.open_movies_page(movie)

# Python-Movie-Website
## Summary
This project will allow the user to make a movie trailer website. The website will contain the movie title,
the storyline, the poster image, and the youtube trailer.
## Download Steps
1. Download python
2. Download the **media.py**, **movie_trailer_site.py**, and **fresh_tomatoes.py** files from [https://github.com/McCode93/Python-Movie-Website]
3. Run **movie_trailer_site.py**
## To Change Movie Selection
1. Go to **movie_trailer_site.py** and look for the following code:
  * toy_story = media.Movie("Toy Story",
                                 "Story about toys.",
                                 "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                 "https://www.youtube.com/watch?v=KYz2wyBy3kc")

  * kisskiss_bangbang = media.Movie("Kiss Kiss, Bang Bang",
                                "All you need to know is that it stars RDJ",
                                "https://upload.wikimedia.org/wikipedia/en/6/61/Kiss_kiss_bang_bang_poster.jpg",
                                "https://www.youtube.com/watch?v=__PnD1HWXSo")

  * scott_pilgrim = media.Movie("Scott Pilgrim",
                            "A movie about a canadian teenager with a dangerous love triangle. Oh, and everyone apparently has super powers.",
                            "https://upload.wikimedia.org/wikipedia/en/1/14/Scott_Pilgrim_vs._the_World_teaser.jpg",
                            "https://www.youtube.com/watch?v=8NUBVcit5VM")
                         
  2. Change the movie names and their corresponding arguments
  3. Find the table **movie** and change the table to fit the new selection. The table will look as follows:
  * movie = [toy_story, kisskiss_bangbang, scott_pilgrim]
  

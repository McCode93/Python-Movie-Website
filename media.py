#imports webbrowser module to open our trailers in a browser
import webbrowser

#create a class to store our movies
class Movie():
    #create __init__ constructor with 5 arguments
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title #self references our new object
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #create a function to open our youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

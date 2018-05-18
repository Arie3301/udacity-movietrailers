import webbrowser


class Movie():
    """Create an instance of a movie with associated data.

    Attributes:
        title: A string with the title of the movie.
        storyline: A string with the storyline of the movie.
        poster_image_url: A string with a url to the movie's poster.
        trailer_youtube_url: A string with a url to a YouTube video of the movie's trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open the trailer URL in a browser."""
        webbrowser.open(self.trailer_youtube_url)

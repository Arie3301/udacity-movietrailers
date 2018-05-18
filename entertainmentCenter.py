import media
import fresh_tomatoes

def main():
    toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    forrest_gump = media.Movie("Forrest Gump", "A story of an imbecile who makes history.", "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg", "https://www.youtube.com/watch?v=77ij5gCTjYU")
    goodfellas = media.Movie("Goodfellas", "The rise and fall of a gangster.", "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg", "https://www.youtube.com/watch?v=qo5jJpHtI1Y")
    lion_king = media.Movie("The Lion King", "Hamlet on the Savanah.", "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg", "https://www.youtube.com/watch?v=4sj1MT05lAA")
    hercules = media.Movie("Hercules", "The son of Zeus must earn his place back among the gods.", "https://upload.wikimedia.org/wikipedia/en/6/65/Hercules_%281997_film%29_poster.jpg", "https://www.youtube.com/watch?v=ZvtspevZxpg")
    oceans_11 = media.Movie("Ocean's Eleven", "A gang of eleven makes a casino heist.", "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg", "https://www.youtube.com/watch?v=imm6OR605UI")

    movies = [toy_story, forrest_gump, goodfellas, lion_king, hercules, oceans_11]
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()

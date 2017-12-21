import webbrowser
import os
import re

# Get the absolute path of the templates directory
TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates')

# Reads the content from the template file.
def read_template(template_file):
    content = ""
    with open(os.path.join(TEMPLATE_DIR, template_file)) as f:
        content = f.read()
    return content

# Styles and scripting for the page
main_page_head = read_template('main_head.html')

# The main page layout and title bar
main_page_content = read_template('main_page_content.html')

# A single movie entry html template
movie_tile_content = read_template('movie_tile_content.html')


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            release_date=movie.release_date,
            storyline=movie.storyline
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

with open("create.txt", "w") as movies_list:
    movie_titles = []

    response = requests.get(URL).text
    soup = BeautifulSoup(response, 'html.parser')
    movies = soup.find_all(name='h3')

    for movie in movies:
        movie_titles.append(movie.text)

    for i in range(len(movie_titles)-1,-1,-1):
        movies_list.write(f"{movie_titles[i]}\n")

import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

movie_titles = soup.select(".article-title-description__text h3.title")

movies = [f"{title.get_text()}\n" for title in movie_titles]
print(movies)


with open("movies.txt", "w") as df:
    df.writelines(movies[::-1])

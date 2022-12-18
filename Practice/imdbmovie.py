import openpyxl
from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
# print(response)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'IMDB Top 250 Movies'
sheet.append(['Rank', 'Movies Name', 'Release Year', 'IMDB Rating'])

movies = soup.find('tbody', class_="lister-list").find_all('tr')
# print(movies)
# print(len(movies))
for movie in movies:
    rank = movie.find('td', class_='titleColumn').get_text(strip=True).split(".")[0]
    movie_name = movie.find('td', class_='titleColumn').a.text
    year = movie.find('td', class_='titleColumn').span.text.strip("()")
    rating = movie.find('td', class_='ratingColumn imdbRating').strong['title']
    sheet.append([rank, movie_name, year, rating])
excel.save('../imdb_top_movies_list.xlsx')

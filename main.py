import requests
from bs4 import BeautifulSoup

URL = "https://www.whoscored.com/Statistics"

page = requests.get(URL).text

with open("footballstats.html", "w") as file:
    file.write(page)

with open("footballstats.html") as file:
    soup = BeautifulSoup(file, "html.parser")

titles = soup.find_all(name="h3", class_="title")

with open("footballstats.csv", "a") as file:
    for title in reversed(titles):
        file.write(f"{title.string}\n")



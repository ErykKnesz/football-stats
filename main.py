import csv

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

URL = "https://www.whoscored.com/Statistics"
team_statistics_id = "top-team-stats-summary-grid"
player_statistics_id = "top-player-stats-summary-grid"

chrome_driver_path = "/home/eryk/Development/108/chromedriver_linux64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(URL)
WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located(
        (By.ID, team_statistics_id)))

html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')

teams_table = soup.find(id=team_statistics_id)
players_table = soup.find(id=player_statistics_id)


with open('teams.csv', 'w', newline='') as teams_csv:
    rows = []
    writer = csv.writer(teams_csv, delimiter=' ')
    for child in teams_table.children:
        for table_row in child.children:
            data_row = []
            for cell in table_row.stripped_strings:
                if cell == "Discipline":
                    yellow = "Yellow Cards"
                    red = "Red Cards"
                    data_row.append(yellow)
                    data_row.append(red)
                else:
                    data_row.append(cell)
            rows.append(data_row)
    writer.writerows(rows)

with open('players.csv', 'w', newline='') as players_csv:
    rows = []
    writer = csv.writer(players_csv, delimiter=' ')
    for child in teams_table.children:
        for table_row in child.children:
            data_row = []
            for cell in table_row.stripped_strings:
                if cell == "Discipline":
                    yellow = "Yellow Cards"
                    red = "Red Cards"
                    data_row.append(yellow)
                    data_row.append(red)
                else:
                    data_row.append(cell)
            rows.append(data_row)
    writer.writerows(rows)







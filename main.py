from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.whoscored.com/Statistics"
team_statistics_id = "top-team-stats-summary-grid"
player_statistics_id = "top-player-stats-summary-grid"

chrome_driver_path = "/home/eryk/Development/108/chromedriver_linux64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(URL)

teams_table = driver.find_elements(By.ID, team_statistics_id)
players_table = driver.find_elements(By.ID, player_statistics_id)





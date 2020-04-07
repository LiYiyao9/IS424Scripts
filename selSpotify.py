import time
import csv
import pandas as pd
from time import sleep
import os.path
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions as selexcept
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


url="https://open.spotify.com/search"
file = open(r'C:\Users\Li Yiyao\Desktop\Codes\DM_Music\songnames.csv','r')
driver = webdriver.Chrome(r'C:\Users\Li Yiyao\Desktop\Codes\Chrome79\chromedriver.exe')
driver.implicitly_wait(120)
driver.get(url)
driver.maximize_window()

final = []
link_array = []
temp = []
try:
    # Open and read CSV file that contains the survey result 
    csv_reader = csv.reader(file,delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        driver.implicitly_wait(120)
        # Locate the search bar of spotify web app
        element = driver.find_element(By.TAG_NAME,'input')
        # Input the user's song and artist into the search bar
        element.send_keys(row[0])
        sleep(randint(2,3))
        # Locate the matching song url as it is in the top of the result
        links = driver.find_elements(By.TAG_NAME,"a")
        # Extract the song ID
        for link in links:
            if "track/" in link.get_attribute('href'):
                link_array.append(link.get_attribute('href'))
        temp = [row[0],link_array[0].split("track/")[1]]
        final.append(temp)
        link_array = []
        temp = []
        sleep(randint(2,3))
        driver.get(url)
    # Write to CSV format
    df = pd.DataFrame(final,columns = ['Song Name','Spotify Id'])
    df.to_csv("spotify_Song_Ids_1.csv")
except Exception as e:
    print(e)

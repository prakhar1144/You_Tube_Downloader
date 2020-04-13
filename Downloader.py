import validators
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

for i in range(1, 50):
    URL = str(input("Enter the URL"))

    valid = validators.url(URL)
    if valid == True:
        print("Searching...")
        break
    else:
        print("Invalid URL")
        continue

driver = webdriver.Chrome("C:/Users/Prakhar Pratyush/Desktop/ChromeDriver/chromedriver.exe")
driver.get("http://en.savefrom.net")
driver.find_element_by_id("sf_url").click()
print("Search Box Clicked...")
try:
   element_present = EC.presence_of_element_located((By.ID,"sf_url"))
   WebDriverWait(driver, 20).until(element_present)
   driver.find_element_by_id("sf_url").send_keys(URL)
except TimeoutError:
    print("failed to load page")
try:
   element_present = EC.presence_of_element_located((By.ID,"sf_submit"))
   WebDriverWait(driver, 20).until(element_present)
   driver.find_element_by_id("sf_submit").click()
except TimeoutError:
    print("failed to submit")


try:
   element_present = EC.presence_of_element_located((By.XPATH,'//*[@class="link-group"]/a'))
   WebDriverWait(driver, 20).until(element_present)
   menu_box = driver.find_elements(By.XPATH, '//*[@class="link-group"]/a')
  # images = driver.find_elements(By.XPATH, '//*[@class="subname"]')
   #print(images)
   for i in range(len(menu_box)):
       print(menu_box[i].get_property("text"))
       #print(images[i].get_property("text"))
except TimeoutError:
    print("Options not loaded yet...")



#driver.find_element_by_id("pass").send_keys(passwrd)
#driver.find_element_by_id("u_0_b").click()

import Downloader
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/Prakhar Pratyush/Desktop/ChromeDriver/chromedriver.exe")

choice = input("Enter Your Choice Number")
driver.get("http://en.savefrom.net")
if choice == 2:
   driver.find_element_by_class_name("link link-download no-downloadable subname ga_track_events").click()
elif choice == 1:
    driver.find_element_by_class_name("link link-download subname ga_track_events").click()
elif choice == 3:
    driver.find_element_by_class_name("no-audio link link-download no-downloadable subname ga_track_events").click()
elif choice == 4:
    driver.find_element_by_class_name("no-audio link link-download no-downloadable subname ga_track_events").click()
else:
    print("Invalid choice try again")


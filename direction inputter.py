
# import required modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


PATH="C:\Program Files (x86)\chromedriver.exe"
Destination=input("What is the start point?")

StartPoint=input("What is the destination?")


# assign url in the webdriver object
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.co.in/maps/@29.7228454,-98.6930793,15z")
sleep(2)

# search locations
def searchplace():
    Place = driver.find_element(By.CLASS_NAME,"tactile-searchbox-input")
    Place.send_keys(StartPoint)
    Submit = driver.find_element(By.ID,
        "searchbox-searchbutton")
    Submit.click()
  
searchplace()
  
  
# get directions
def directions():
    sleep(5)
    directions = driver.find_element(By.CLASS_NAME,
        "S9kvJb")
    directions.click()
  
directions()
  

def route():
     sleep(5)
     route = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
     route.send_keys(Destination)
     route.send_keys(u'\ue007')

     


route()


def 

     
  
  

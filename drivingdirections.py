
# import required modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By



PATH="C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('user-agent=fake-useragent')
driver = webdriver.Chrome(PATH, options=options)

Destination=input("What is the start point?")

StartPoint=input("What is the destination?")

Mode=input("What is the mode of transportation?")




# assign url in the webdriver object

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
     sleep(10)
     route = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
     route.send_keys(Destination)
     route.send_keys(u'\ue007')
     sleep(10)
     pasgod = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]")
     pasgod.click()
     sleep(10)
     kawhi = driver.find_element(By.CLASS_NAME, "delay-light")
     sleep(5)
     hello=driver.find_element(By.CLASS_NAME, "M3pmwc")

     print("The eta is"+ " " + "in" + " " + kawhi.text+ ".")
     y=hello.text
     z=y.replace("These directions are for planning purposes only. You may find that construction projects, traffic, weather, or other events may cause conditions to differ from the map results, and you should plan your route accordingly. You must obey all signs or notices regarding your route.","")
     print(z)

route()



     
  
  


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By



PATH="C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

Destination=input("What is the flight number?")



# assign url in the webdriver object

driver.get("https://flightaware.com/")
sleep(10)

route = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div[3]/div/div[2]/div/form/div[1]/ul/li/input")


route.click()
route.send_keys(Destination)
route.send_keys(u'\ue007')
sleep(10)
flight_status=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]")
print(flight_status.text)




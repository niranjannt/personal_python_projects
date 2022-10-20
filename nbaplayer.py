from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By



PATH="C:\Program Files (x86)\chromedriver.exe"



driver = webdriver.Chrome(PATH)

player=input("What is the name of the NBA player?")

driver.get("https://www.statmuse.com/")
sleep(10)
Search=driver.find_element(By.XPATH,"/html/body/main/div[3]/div[2]/div/ask-bar/form/div/div[1]/textarea")
Search.send_keys(player)
Search.send_keys(u'\ue007')
sleep(10)
rebounds=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div[3]/div/div/div[2]/p[2]")
sleep(10)
ppg=driver.find_element(By.CLASS_NAME,"text-3xl")
sleep(10)
assists=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div[3]/div/div/div[3]/p[2]")
sleep(5)
career=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div[3]/div/p")
if career.text=="CAREER":
    print("During his career,"+" "+player+"  "+"averaged"+ "  "+ ppg.text+"  "+ "points,"+  "  "+ rebounds.text+"  "+"rebounds"+"  "+assists.text+"  "+"assists"+" "+"per game.")
          
else:
    print("During the 2021-2022 NBA season," + "  " + player + "  "+ "averaged" + "  " + ppg.text +"  " + "points,"+  "   "+ "and" +"  "+ rebounds.text+"  "+"rebounds"+"  "+assists.text+"  "+"assists"+ " "+ "per game.")

    



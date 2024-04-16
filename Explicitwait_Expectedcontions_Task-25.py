from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from time import sleep





# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Filters:


    def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       # Explicit wait
       self.wait = WebDriverWait(self.driver, 10)


    def boot(self):
       self.wait = WebDriverWait(self.driver, 10)
       self.driver.get(self.url)
       self.driver.maximize_window()
       #self.wait.until(ec.url_to_be(self.url))

       
    def fillName(self,Name):
       self.wait = WebDriverWait(self.driver, 10)
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Name)
       sleep(5)
       
    def fillBirthdate(self,Birthdate):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Birthdate)
       sleep(5)
       
    def fillBirthday(self,Birthday):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[3]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Birthday)
       sleep(5)
       
    def fillAwardsrecognition(self,Awardsrecognition):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[4]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Awardsrecognition)
       sleep(5)
       
    def fillPagetopics(self,Pagetopics):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[5]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Pagetopics)
       sleep(5)
       
    def fillDeathdate(self,Deathdate):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[6]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Deathdate)
       sleep(5)
       
       
    def fillGenderidentity(self,Genderidentity):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Genderidentity)
       sleep(5)
       
       
    def fillCredits(self,Credits):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[8]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Credits)
       sleep(5)
       
       
    def fillAdultnames(self,Adultnames):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[9]/div[1]/label"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Adultnames)
       sleep(5)
       
       
    def clickSeeresults(self,Seeresults):
       fullXPath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button".click()
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       #element.send_keys(Searchfilters)
       element.click(Seeresults)
       sleep(5)
       
    


obj = Filters("https://www.imdb.com/search/name//")
obj.boot()
obj.fillName("Tharani")
obj.fillBirthdate("05-05-1990")
obj.fillBirthday("10-10")
obj.fillAwardsrecognition("Best Acterss-Nominated")
obj.fillPagetopics("Biography")
obj.fillDeathdate("10-10-2090")
obj.fillGenderidentity("Male")
obj.fillCredits("100")
obj.fillAdultnames("Include")
obj.clickSeeresults(Seeresults)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

START_URL = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
EMAIL = ""
PASSWORD = ""

chrome_driver_path = "./drivers/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(START_URL)
time.sleep(2)

email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)

pword = driver.find_element(By.ID, "password")
pword.send_keys(PASSWORD)

sign_in = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in.click()
time.sleep(2)

job_icon = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div/li-icon')
job_icon.click()
time.sleep(5)

job_search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
job_search.send_keys("Python")
job_search.send_keys(Keys.ENTER)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "./drivers/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# to click on the same link whose count we just printed
# article_count.click()

# easier way of clicking links on a page
# wikinews = driver.find_element(By.LINK_TEXT, "Wikinews")
# wikinews.click()

# type something in an input box
# search_box = driver.find_element(By.NAME, "search")
# search_box.send_keys("Python")
# use enter key
# search_box.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Python")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("ista")

email = driver.find_element(By.NAME, "email")
email.send_keys("pythonista@python.com")

# click on sign up button
sign_up = driver.find_element(By.CLASS_NAME, "btn-primary")
sign_up.click()

driver.quit()
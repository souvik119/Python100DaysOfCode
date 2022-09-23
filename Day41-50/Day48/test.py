from selenium import webdriver

chrome_driver_path = "./drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# opens up a new browser window with the specified address
driver.get("https://www.amazon.com")

# close the active window
# driver.close()

# quit the entire browser
driver.quit()
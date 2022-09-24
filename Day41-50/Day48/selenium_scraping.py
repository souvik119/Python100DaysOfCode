from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "./drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

timestamp_list = [times.text for times in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]
event_name_list = [event.text for event in driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")]

events = {}
for n in range(len(event_name_list)):
    events[n] = {
        "time": timestamp_list[n],
        "event": event_name_list[n],
    }

print(events)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
#slider=driver.find_elements(By.CLASS_NAME, 'homeslider-container')
#print(len(slider))

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

input("Press Enter to close the browser...")
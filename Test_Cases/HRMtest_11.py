from selenium import webdriver
from selenium.webdriver.common.by import By

import time

"""
test-11
     1.login
     2.job details
     3.activate employee
     4.job activated
     
"""



driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
#click PIM Module
driver.find_element(By.XPATH,"//span[text()='PIM']").click()
time.sleep(3)
#Search Employee
search=driver.find_element(By.XPATH,"(//input[@placeholder='Type for hints...'])[1]")
time.sleep(3)
search.send_keys("Cassidy  Hope")
time.sleep(3)
ka=driver.find_element(By.XPATH,"//button[@type='submit']")
ka.click()
time.sleep(3)
se=driver.find_element(By.XPATH,"(//i[@class='oxd-icon bi-pencil-fill'])[1]")
se.click()
time.sleep(3)
#Job
job=driver.find_element(By.XPATH,"//a[contains(text(),'Job')]").click()
time.sleep(5)
#Terminate
ter=driver.find_element(By.CSS_SELECTOR,".oxd-button--label-danger").click()
time.sleep(3)
#Date
da=driver.find_element(By.XPATH,"//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--white oxd-dialog-sheet oxd-dialog-sheet--shadow oxd-dialog-sheet--gutters orangehrm-dialog-modal']//input[@class='oxd-input oxd-input--active']")
da.send_keys("2022-12-30")
time.sleep(3)
#Reason
re=driver.find_element(By.XPATH,"//div[@role='document']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']").click()
son=driver.find_element(By.XPATH,"//span[text()='Laid-off']").click()
time.sleep(3)
#Note
note=driver.find_element(By.XPATH,"//textarea[@placeholder='Type here']")
note.send_keys("Due To Lay Off")
time.sleep(3)
#Save
sa=driver.find_element(By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[2]").click()
time.sleep(10)
#Activate
driver.find_element(By.XPATH,"//button[text()=' Activate Employment '] ").click()
time.sleep(3)










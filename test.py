from selenium import webdriver
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
drive.get("http://www.python.org")
drive.find_element(By.ID,'id-search-field').send_keys("python")
drive.find_element(By.CSS_SELECTOR,'#submit').click()

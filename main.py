

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()

driver.get('https://eclass.yorku.ca/eclass/')

f=open("account.txt","r")
lines=f.readlines()
username=lines[0]
password=lines[1]
f.close()

# print("Username: "+username +"\n Password: "+password+"\n")


User_Input=driver.find_element_by_id("mli")
User_Input.send_keys(username)

# driver.find_element_by_id("password").click()



# driver.find_element_by_id("password").send_keys("Test")

driver.switch_to.alert.dismiss()

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).click()
Pwd_Input=driver.find_element_by_id(password)
Pwd_Input.send_keys("passwor1d")

Login_Button=driver.find_element_by_xpath("//*[@type='submit']")
Login_Button.click()







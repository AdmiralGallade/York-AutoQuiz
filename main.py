

from asyncio import wait_for
from multiprocessing.connection import answer_challenge
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pickle 

driver = webdriver.Chrome()

def SaveCookies():
    pickle.dump(driver.get_cookies(), open("cookie_file.pkl", "wb"))

def readCookies():
    cookies = pickle.load(open("cookie_file.pkl", "rb")) 
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

def main():
    

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

    try:
        driver.switch_to.alert.dismiss()
    except NoAlertPresentException:
        print("alert not found")

    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).click()
    Pwd_Input=driver.find_element_by_xpath("//*[@type='password']")
    Pwd_Input.send_keys(password)

    Login_Button=driver.find_element_by_xpath("//*[@type='submit']")
    Login_Button.click()




    new_url = 'https://eclass.yorku.ca/mod/quiz/view.php?id=1907631'

    driver.get(new_url)

    submitOrContinueButton= driver.find_element_by_xpath("//*[@type='submit']")
    submitOrContinueButton.click()

    i=0
    numberOfQuestions=10
    questionsSet=dict()
    nextPageButton=driver.find_element_by_xpath('//*[@value="Next page"]')

    for i in range(numberOfQuestions)

        answerChoiceNum=len(driver.find_elements_by_xpath('//*[@class="answernumber"]'))
        questionsSet[i]=answerChoiceNum
        nextPageButton.click()
        i+=1
        
driver.close()



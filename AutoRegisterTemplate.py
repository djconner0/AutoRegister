from datetime import datetime
import time
from selenium import webdriver
i = 0
TdDate = datetime.now().strftime("%m-%d %H:%M")
RegistDate = "MM-DD HH:MM"
while 1 < 2:

    if TdDate == RegistDate:

        driver = webdriver.Chrome()
        driver.get('https://sso.uah.edu/cas/login?service=https%3A%2F%2Fmy.uah.edu%2Fc%2Fportal%2Flogin')

        ChIDLogin = driver.find_element_by_xpath('//*[@id="username"]')
        ChIDLogin.send_keys('dc0131')
        time.sleep(0.05)

        PassLogin = driver.find_element_by_xpath('//*[@id="password"]')
        PassLogin.send_keys('Dylpickle38459270*')

        LoginButton = driver.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[4]')
        LoginButton.click()


        driver.get('https://uah.collegescheduler.com/entry')


        CartLink = driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[13]/td[2]/a')
        CartLink.click()

        TermSubButt = driver.find_element_by_xpath('/html/body/div[3]/form/input')
        TermSubButt.click()

        while i < 5:
            now = datetime.now().time()
            current_time = now.strftime("%H:%M")
            regist_time = "HH:MM"
            if current_time == regist_time:
                RegButt = driver.find_element_by_xpath('/html/body/div[3]/form/input[1]')
                RegButt.click()
                driver.back()
                i += 1

        RegButt = driver.find_element_by_xpath('/html/body/div[3]/form/input[1]')
        RegButt.click()
    if i >= 5:
        break
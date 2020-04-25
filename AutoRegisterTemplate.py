# Importing datetime, time, selenium
from datetime import datetime
import time
from selenium import webdriver
# Defines a count variable used for later
i = 0
# TdDate is Today's date, RegistDate is the Register day and
# however many minutes before Registration you choose to open up
# the registration page. I use 1 minute for reasons seen below
# RegistDate NEEDS TO BE CHANGED TO REFLECT SCHEDULE
TdDate = datetime.now().strftime("%m-%d %H:%M")
RegistDate = "MM-DD HH:MM"
# Loop to check set time for when to login and navigate to
# registration page. 
while 1 < 2:

    if TdDate == RegistDate:

        #Points script to Login site
        
        driver = webdriver.Chrome()
        driver.get('https://sso.uah.edu/cas/login?service=https%3A%2F%2Fmy.uah.edu%2Fc%2Fportal%2Flogin')
        
        #Inserts User and Pass, sleeps because it doesn't like it too fast
        
        ChIDLogin = driver.find_element_by_xpath('//*[@id="username"]')
        ChIDLogin.send_keys('USERNAME')
        time.sleep(0.05)

        PassLogin = driver.find_element_by_xpath('//*[@id="password"]')
        PassLogin.send_keys('PASSWORD')

        # clicks login button

        LoginButton = driver.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[4]')
        LoginButton.click()

        # Navigates to Schedule Cart, cookie is saved on chrome
        
        driver.get('https://uah.collegescheduler.com/entry')

        # Clicks a couple buttons to move to register

        CartLink = driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[13]/td[2]/a')
        CartLink.click()

        TermSubButt = driver.find_element_by_xpath('/html/body/div[3]/form/input')
        TermSubButt.click()

        # Checks for the correct time so that it registers at exact time
        # This runs 5 times because I don't trust it

        while i < 5:

            # Compares current time to registration time, THIS NEEDS TO
            # BE EDITED TO REFLECT SCHEDULE

            now = datetime.now().time()
            current_time = now.strftime("%H:%M")
            regist_time = "HH:MM"

            # This clicks the register button and returns to previous page

            if current_time == regist_time:
                RegButt = driver.find_element_by_xpath('/html/body/div[3]/form/input[1]')
                RegButt.click()
                driver.back()
                i += 1

        #This clicks the register buton one last time

        RegButt = driver.find_element_by_xpath('/html/body/div[3]/form/input[1]')
        RegButt.click()

        # Here's the count variable, it breaks the loop

    if i >= 5:
        break
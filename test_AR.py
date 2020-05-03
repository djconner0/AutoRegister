# Importing datetime, time, selenium
from datetime import datetime
import time
from selenium import webdriver

# Defines a count variable used for later
i = 0

#Gets Registration Date
print('Registration MM-DD:')
RegistDate = input()

#Gets Registration Time (probably a better way to do this)
print('Registration HH:')
RegistHour = input()
print('Registration MM:')
RegistMin = input()
RegistTime = str(RegistHour + ':' + RegistMin)

#This sets the time for the browser to open
if RegistMin == '00':
    RegistMin = '59'
    RegistHour = '0' + str(int(RegistHour) - 1)
else:
    RegistMin = str(int(RegistMin) - 1)

#Login time
LoginTime = str(RegistDate + ' ' + RegistHour + ':' + RegistMin)
#Gets Username and Password for login
print('Charger ID:')
Username = input()
print('Password:')
Password = input()

# Loop to check the time for when to login and navigate to
# registration page. 
while i < 5:

    #Gets the current date based on machine time
    TdDate = datetime.now().strftime("%m-%d %H:%M")

    if TdDate == TdDate:

        #Points script to Login site
        
        driver = webdriver.Chrome()
        driver.get('https://sso.uah.edu/cas/login?service=https%3A%2F%2Fmy.uah.edu%2Fc%2Fportal%2Flogin')
        
        #Inserts User and Pass, sleeps because it doesn't like it too fast
        
        ChIDLogin = driver.find_element_by_xpath('//*[@id="username"]')
        ChIDLogin.send_keys(Username)
        time.sleep(0.05)

        PassLogin = driver.find_element_by_xpath('//*[@id="password"]')
        PassLogin.send_keys(Password)

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
            CurrentTime = now.strftime("%H:%M")

            # This clicks the register button and returns to previous page

            if CurrentTime == CurrentTime:
                RegButt = driver.find_element_by_xpath('/html/body/div[3]/form/input[1]')
                RegButt.click()
                driver.back()
                i += 1

        #This clicks the register button one last time

        RegButt = driver.find_element_by_xpath('/html/body/div[3]/form/input[1]')
        RegButt.click()

    #This sleeps to play nice with your cpu

    time.sleep(10)
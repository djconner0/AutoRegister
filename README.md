# AutoRegister
This is an Auto Registration Script for UAH.

Prerequisites:
  Python3
  Selenium
  Chrome Webdriver (Can be replaced by Firefox or IE, but Chrome doesn't clean cookies and it works)
  
Script must be modified to work for each individual since I just threw this together.
    
    Line 6: RegistDate = "MM-DD HH:MM" replace with the scheduled registration date. The time I usually set for 1 minute before
    Line 15: ChIDLogin.send_keys('USERNAME') replace with your UAH username
    Line 19: PassLogin.send_keys('PASSWORD') replace with your UAH password
    Line 37: regist_time = "HH:MM" replace with the exact registration time

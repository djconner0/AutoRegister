# AutoRegister
This is an Auto Registration Script for UAH.

How to run it (Linux):
  Open up a terminal
  Navigate to the script
  >python3 AutoRegister2020.py

How to run it (Windows):
	Open it in the python IDLE
  Run > Run Module
  ps if you can install selenium and the driver on windows... let me know.

  The test script can be run the same way. It just runs the bot when you give it login creds.


Prerequisites:
  Python 3
  Selenium
  Chrome Webdriver (Can be replaced by Firefox or IE, but Chrome doesn't clean cookies and it works)
  
Input examples (ensure that format is followed):
  Registration MM-DD: 05-04
  Registration HH: 08
  Registration MM: 00
  Charger ID: username
  Password: password
  
Login details are sent straight to the my.uah.edu login page, you can verify in source.
If I can't figure out an easier way to do inputs, I also can't figure out how to steal login creds.

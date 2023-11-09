# Test to ensure selenium properly installed with pip install along with gekko driver
# gekko driver from https://github.com/mozilla/geckodriver/releases
# Tutorial by John Watson Rooney https://www.youtube.com/watch?v=pUUhvJvs-R4&list=PLRzwgpycm-FgQ9lP_JTfrCa9O573XiJph&index=1
# Using a dummy site for practice https://the-internet.herokuapp.com/login

# selenium installed to python version 3.10.5 and version 3.12.0
# "Import request" error will show if using python version without selenium installed

"""
Test .py file uses selenium with gekko driver (for use with Firefox) to 
1. Open Firefox browser 
2. Go to dummy website URL 
3. Send information to populate login info fields 
4. Login to dummy website
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# url = "http://google.com"
url = "https://the-internet.herokuapp.com/login"

# When executing .py file, will open up browser to specified url
driver.get(url)

# In tutorial, John uses find_element_by_xpath function which has been removed from Selenium
# Use find_element("xpath", '//*[@id=""]') instead

driver.find_element("xpath", '//*[@id="username"]').send_keys('tomsmith')
driver.find_element("xpath", '//*[@id="password"]').send_keys('SuperSecretPassword!')
driver.find_element("xpath", '//*[@id="login"]/button').click()

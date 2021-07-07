import unittest
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox

'''
INSTRUCTIONS:
Using the language of your choice, write code that utilizes Selenium Webdriver (https://www.selenium.dev/documentation/en/webdriver/) to complete the following steps in a browser.

Navigate to “www.google.com”

Select the Main Search Box and enter the text “RTS Labs”

Click “Google Search” or press the Enter key to execute the search and await the results

Click the first result URL from the search (Normally this will be the RTS Website)
ADDENDUM
I've gone ahead and put this in the form of test cases using python for the 'Big Three' Web browsers, and they all run sucesssfully on my machine
'''

class TestWeb(unittest.TestCase):
    def SeleniumTest(self,driver):
        driver.get("https://www.google.com/")

        #Honestly, no clue why the Google Search bar's Element is named 'q' but here we are
        SearchField = driver.find_element_by_name("q")

        SearchField.send_keys("RTS Labs" + Keys.RETURN)
        #Wait for the google resutls to load, or 30 seconds, the google results URLS are HTML tagged H3, so if we get a list of all of them, then we know the first one is the first result
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        result = driver.find_elements_by_tag_name("h3");

        result[0].click()
        # Wait for page load (30 Seconds, or until the browser finds the element labeled 'top', which on the RTS labs site is the green bar at the top of the screen)  
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'top')))
        except TimeoutError:
            print("slow")

        self.assertEqual("https://rtslabs.com/",driver.current_url)
        driver.quit() #Close out of the web page

    def test_Firefox(self): 
        driver = webdriver.Firefox()
        TestWeb.SeleniumTest(self,driver)

    def test_Chromium(self):
        driver = webdriver.Chrome()
        TestWeb.SeleniumTest(self,driver)

    def test_Edge(self):
        driver = webdriver.Edge()
        TestWeb.SeleniumTest(self,driver)

if __name__ == '__main__':
    unittest.main()


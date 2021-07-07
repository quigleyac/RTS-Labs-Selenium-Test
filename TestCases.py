import unittest
from selenium import webdriver
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
    def test_Firefox(self): # The First one i wrote, Check here for Comments
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/")

        SearchField = driver.find_element_by_name("q") 
        SearchField.send_keys("RTS Labs" + Keys.RETURN)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        result = driver.find_elements_by_tag_name("h3");
        result[0].click()
        # Wait for page load  
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'top')))
        except TimeoutError:
            print("slow")

        self.assertEqual("https://rtslabs.com/",driver.current_url)
        driver.quit()

    def test_Chromium(self):
        driver = webdriver.Chrome()

        driver.get("https://www.google.com/")

        SearchField = driver.find_element_by_name("q") 
        SearchField.send_keys("RTS Labs" + Keys.RETURN)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        result = driver.find_elements_by_tag_name("h3");
        result[0].click()
        # Wait for page load    
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'top')))
        except TimeoutError:
            print("slow")
        self.assertEqual("https://rtslabs.com/",driver.current_url)
        driver.quit()

    def test_Edge(self):
        driver = webdriver.Edge()

        driver.get("https://www.google.com/")

        SearchField = driver.find_element_by_name("q") 
        SearchField.send_keys("RTS Labs" + Keys.RETURN)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        result = driver.find_elements_by_tag_name("h3");
        result[0].click()
        # Wait for page load
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'top')))
        except TimeoutError:
            print("slow")

        self.assertEqual("https://rtslabs.com/",driver.current_url)
        driver.quit()

if __name__ == '__main__':
    unittest.main()


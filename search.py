from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Use the correct path to the chromedriver executable
driver_path = r"C:\Users\patel\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Initialize WebDriver
web = webdriver.Chrome(service=service)


    # Navigate to the website
web.get("https://shop.bewakoof.com/")
    
    # Allow some time for the page to load
time.sleep(1)
    
    # Find the login input field and enter the phone number
search = web.find_element(By.XPATH, "/html/body/div/main/header/div/div[2]/div[2]/ul/li/div/div/div/div/form/li/input")
time.sleep(2)
search.send_keys("shirt")
time.sleep(2)
search.send_keys(Keys.RETURN)

time.sleep(2.5)

first = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[1]/div/main/div/section[2]/section/section[1]/a/figure/img"))
    )
first.click()

time.sleep(2.5)

    # Wait for user input to close the browser
input("Press Enter to close the browser...")


    # Close the WebDriver session
web.quit()
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

# Navigate to the Bewakoof website
web.get("https://shop.bewakoof.com/")

# Wait for 1 second to ensure the page has fully loaded
time.sleep(1)

# Click the login button to open the login form
login_button = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/header/div/div[2]/div[2]/ul/a[1]/span"))
)
login_button.click()

time.sleep(2.5)

# Wait for the phone number input field to be present and enter the phone number
phone_input = WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/section/div[2]/div[2]/form/div/div[1]/div/input"))
)
phone_input.send_keys("9741246631")

# Wait for 2.5 seconds before clicking the continue button
time.sleep(2.5)

# Wait until the continue button is clickable and click it
continue_button = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/section/div[2]/div[2]/form/div/div[2]/input"))
)
continue_button.click()

time.sleep(2.5)

# Wait for user input to close the browser
input("Press Enter to close the browser...")

# Close the WebDriver session
web.quit()

import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

load_dotenv()

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
PHONE = "999999999"

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

# Reject cookies
# time.sleep(2)
# reject_button = driver.find_element(By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign In Button
time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# If captcha is presented - solve manually
# input("Press Enter when you have solved the Captcha")

time.sleep(5)

# Get listings
all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening listing")
    print(listing)
    try:
        listing.click()
        time.sleep(3)

        # Try to find and click the save button
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")

        aria_pressed = save_button.get_attribute("aria-pressed")

        if aria_pressed is not None:
            if aria_pressed == "false":
                save_button.click()
                print("Job saved (aria)")
            else:
                print("Already saved (aria)")
        else:
            # Fallback: check visible text
            span = save_button.find_element(By.CLASS_NAME, "jobs-save-button__text")
            if "Salvar" in span.text:
                save_button.click()
                print("Job saved (text fallback)")
            else:
                print("Already saved (text fallback)")

        time.sleep(2)

    except NoSuchElementException:
        print("Save button not found, skipping...")
        continue

time.sleep(5)
driver.quit()
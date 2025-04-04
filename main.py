import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

load_dotenv()

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
PHONE = "999999999"
YEARS_OF_XP = "1"

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

# Locate apply button
time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

# If the application requires phone number and the field is empty, then fill in the number
time.sleep(5)
phone = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4195448559-10862781777-phoneNumber-nationalNumber"]')
if phone.text == "":
    phone.send_keys(PHONE)

time.sleep(2)
# Next step 1
submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
submit_button.click()

# Next step 2
time.sleep(2)
submit_button.click()

years_of_xp = driver.find_element(By.CSS_SELECTOR, value="#ember402 input")
if years_of_xp.get_attribute("value") == "":
    years_of_xp.send_keys(YEARS_OF_XP)

time.sleep(2)
revision_btn = driver.find_element(By.ID, value="ember403")
revision_btn.click()

# Send CV Button
send_cv_btn = driver.find_element(By.ID, value="ember414")
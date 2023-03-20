import os
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3532443930&f_AL=true&geoId=103697962&keywords=python%20developer&location=Ho%20Chi%20Minh%20City%2C%20Vietnam&refresh=true")


# LOGIN STEP
sign_in_button = driver.find_element(By.CSS_SELECTOR, ".nav__cta-container a.nav__button-secondary")
sign_in_button.click()

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(USERNAME)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(5)

# SAVE JOB
job_posts = driver.find_elements(By.CSS_SELECTOR, '.job-card-container')[:10]

for job_post in job_posts:
    try:
        job_post.click()

        time.sleep(3)
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()

        time.sleep(1)
        close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
        close_button.click()

        time.sleep(1)
        discard_button = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button--secondary')
        discard_button.click()
    # If already applied for this job or job is no longer accepting applications, then skip
    except NoSuchElementException:
        print("No application button, skipped.")
        continue


driver.quit()


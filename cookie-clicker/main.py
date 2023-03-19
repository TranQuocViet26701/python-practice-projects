import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

item_name_tags = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_names = [item.get_attribute("id") for item in item_name_tags]

timeout = time.time() + 5
five_mins = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() >= timeout:
        item_price_tags = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        item_prices = []
        for item in item_price_tags:
            if item.text:
                item_prices.append(int(item.text.split(" - ")[1].replace(",", "")))

        cookie_upgrades = {}
        for i in range(len(item_prices)):
            cookie_upgrades[item_prices[i]] = item_names[i]

        current_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        affordable_upgrades = {}
        for cost, name in cookie_upgrades.items():
            if current_money > cost:
                affordable_upgrades[cost] = name

        highest_price = max(affordable_upgrades)
        print(highest_price)
        to_purchase_name = affordable_upgrades[highest_price]

        driver.find_element(By.ID, to_purchase_name).click()

        timeout += 5

    if time.time() >= five_mins:
        cookie_per_second = driver.find_element(By.ID, "cps").text
        print(cookie_per_second)
        break

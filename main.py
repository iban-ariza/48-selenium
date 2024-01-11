"""
Selenium is much shorter because we don't have to take care of the requests being made.
It also takes care of AngularJS, React, etc, which beautifulsoup has trouble with.

This script goes and checks the price of an Amazon item.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.amazon.com"
instant_pot_url = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS"


# opens the url, but immediately closes it too
driver.get(instant_pot_url)

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")  # returns a WebElement
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"The price is: {price_dollar.text}.{price_cents.text}")  # access text with dot notation (selenium object.text)


# driver.close()    # closes the tab from the web browser
driver.quit()     # closes the entire web browser

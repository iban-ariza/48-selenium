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
url = "https://www.python.org/"

# opens the url, but immediately closes it too
driver.get(url)

# returns WebElement: <selenium.webdriver.remote.webelement.WebElement (session="c9746bd", element="1A3297_element_5")>
search_bar = driver.find_element(By.NAME, "q")  # use the inspect to check the html
print(search_bar)
print(search_bar.tag_name)  # print tag name
print(search_bar.get_attribute("placeholder"))  # gets the attribute value from the attribute name

button = driver.find_element(By.ID, "submit")
print(button)

# get anchor (with no id/class), but inside a div with class documentation-widget
# you can get CSS Selector from inspect's copy
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# find element through Xpath (you can get Xpath from inspect copy)
bug_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(f"Submit Website Bug Link: {bug_link.text}")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
print(f"Event times: {event_times}")
for event_time in event_times:
    print(event_time.text)

# driver.close()    # closes the tab from the web browser
driver.quit()     # closes the entire web browser

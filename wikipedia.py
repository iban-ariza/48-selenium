from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)


# --------------- WAYS TO CLICK -------------------

num_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount > a:nth-child(1)")
print(num_articles.text)
# num_articles.click()    # click on the link that you found from the website

# click on element based on the text of the link
encyclopedia_link = driver.find_element(By.LINK_TEXT, value="encyclopedia")
# encyclopedia_link.click()

# click using a keyboard key (get search element -> typing Python -> clicking ENTER)
# search = driver.find_element(By.NAME, "search")
search = driver.find_element(By.XPATH, "//*[@id='searchInput']")

# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


driver.close()




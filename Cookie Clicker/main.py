import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from collections import OrderedDict

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = Service("C:\Development\chromedriver")
driver = webdriver.Chrome(options=options, service=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


timeout = time.time() + 5

while True:
    cookie.click()

    if time.time() > timeout:
        prices = {}
        store = driver.find_elements(By.CSS_SELECTOR, '[id="store"] div')
        for i in store:
            try:
                price = i.find_element(By.TAG_NAME, "b").get_attribute("textContent")
            except selenium.common.exceptions.NoSuchElementException:
                price = "Factory -  500"
            else:
                pass
            finally:
                name = i.get_attribute("id")
                price = price.split("-")
                p = int(price[1].replace(",", "").strip())
                prices[name] = p
        max = 0
        score = driver.find_element(By.ID, "money").get_attribute("textContent")
        score = int(score.replace(",", "").strip())
        res = dict(reversed(list(prices.items())))
        for a in res:
            if score >= res[a]:
                driver.find_element(By.ID, f"{a}").click()
                break
        timeout = time.time() + 5


driver.close()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = Service("C:\Development\chromedriver")
driver = webdriver.Chrome(options=options, service=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
# href = sign_in.get_attribute("href")
# driver.get("/html/body/div[1]/header/nav/div/a[2]")
driver.find_element(By.ID, "username").send_keys("mitultiwari35@gmail.com")
driver.find_element(By.ID, "password").send_keys("Tatoout1")
driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
# a = driver.find_elements(By.CLASS_NAME, 'full-width artdeco-entity-lockup__title ember-view')
# print(a)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '[class="jobs-s-apply jobs-s-apply--fadein inline-flex mr2"] [class="jobs-apply-button--top-card"] button').click()
time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3656983339-720017503049330542-phoneNumber-nationalNumber"]').send_keys("8989000595")
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span').click()
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[1]/div/div/div[1]/div/input').send_keys('291/15 MR-6')
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[2]/div/div/div[1]/div/input').send_keys('Mahalxmi Nagar')
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div/div/div/input').send_keys('Indore, Madhya Pradesh, India')
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div/div/div/input').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]/span').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button/li-icon/svg').click()
# driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[2]/button[2]/span').click()



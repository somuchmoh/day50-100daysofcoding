from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.flaticon.com/")

signup = driver.find_element(By.CLASS_NAME, "login-register-user-button")
signup.click()

time.sleep(5)
fb_login = driver.find_element(By.CLASS_NAME, "main-button")
fb_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = driver.find_element(By.NAME, "email")
email_input.click()
email_input.send_keys("my_email")

pwd_input = driver.find_element(By.NAME, "pass")
pwd_input.click()
pwd_input.send_keys("password")
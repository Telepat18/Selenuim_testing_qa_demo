from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# options


url = "https://www.instagram.com/"
driver = webdriver.Chrome(
    executable_path="/Users/proarea/PycharmProjects/Selenium/chromeDriver/chromedriver")
# C:\\users\\ for windows

try:
    driver.get(url=url)
    time.sleep(5)

    email_field = driver.find_element(By.NAME, "username")
    email_field.clear()
    email_field.send_keys("roma.testing")
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("Google00-")
    login_button = driver.find_element(By.CLASS_NAME, "_ab8w._ab94._ab99._ab9f._ab9m._ab9p._abcm")
    login_button.click()
    time.sleep(5)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

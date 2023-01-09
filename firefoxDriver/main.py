from selenium import webdriver
import time


url = "https://www.instagram.com/"
driver = webdriver.Firefox(executable_path="/Users/proarea/PycharmProjects/Selenium/firefoxDriver/geckodriver")
# C:\\users\\ for windows
try:
    driver.get(url=url)
    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

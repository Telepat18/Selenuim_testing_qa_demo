from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import List


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)



    def get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'tag': By.TAG_NAME,
            'partial': By.PARTIAL_LINK_TEXT
        }
        return locating[find_by]

    def is_visiable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_visiable(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)

    def element_is_clickable(self, find_by: str, locator: str, locator_name: str = None):
        return self.wait.until(EC.element_to_be_clickable((self.get_selenium_by(find_by), locator)), locator_name)

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)




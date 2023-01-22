from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)

    @staticmethod
    def get_selenium_by(find_by) -> dict:
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

    def is_visible(self, find_by: str, locator, locator_name: str = None):
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None):
        return self.wait.until(ec.presence_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None):
        return self.wait.until(ec.invisibility_of_element_located((self.get_selenium_by(find_by), locator)),
                               locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None):
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)),
                               locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None):
        return self.wait.until(ec.presence_of_all_elements_located((self.get_selenium_by(find_by), locator)),
                               locator_name)

    def element_is_clickable(self, find_by: str, locator, locator_name: str = None):
        return self.wait.until(ec.element_to_be_clickable((self.get_selenium_by(find_by), locator)),
                               locator_name).click()

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()


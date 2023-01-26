import requests

from selenium_base.base import SeleniumBase


class LinksPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.link_item = 'li[id="item-5"]'
        self.simple_link = 'a[id="simpleLink"]'
        self.dynamic_link = 'a[id="dynamicLink"]'
        self.created_link = 'a[id="created"]'
        self.no_content = 'a[id="no-content"]'
        self.moved = 'a[id="moved"]'
        self.bad_request = 'id="bad-request"'
        self.unauthorized = 'a[id="unauthorized"]'
        self.forbidden = 'a[id="forbidden"]'
        self.invalid_url = 'a[id="invalid-url"]'
        self.link_href = 'url'

    def find_link_item(self):
        return self.is_visible('css', self.link_item)

    def check_new_tab_simple_link(self):
        simple = self.is_visible('css', self.simple_link)
        link_href = simple.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_bad_request(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.is_visible('css', self.bad_request).click()
        else:
            return request.status_code

    def check_created(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.is_visible('css', self.created_link).click()
        else:
            return request.status_code

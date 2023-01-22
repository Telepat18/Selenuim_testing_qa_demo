from selenium_base.base import SeleniumBase


class UploadDownloadPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

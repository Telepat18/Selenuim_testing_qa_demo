import base64
import os
import random

from generator.generator import generated_file
from selenium_base.base import SeleniumBase


class UploadDownloadPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.upload_item = '#item-7'
        self.upload_file = 'input[id="uploadFile"]'
        self.uploaded_result = 'p[id="uploadedFilePath"]'
        self.download_file = 'a[id="downloadButton"]'

    def find_upload_item(self):
        item = self.is_present('css', self.upload_item)
        self.go_to_element(item)
        item.click()

    def upload_files(self):
        file_name, path = generated_file()
        self.is_present('css', self.upload_file).send_keys(path)
        os.remove(path)
        text = self.is_present('css', self.uploaded_result).text
        return file_name.split('/')[-1], text.split('\\')[-1]

    def download_files(self):
        link = self.is_present('css', self.download_file).get_attribute('href')
        link_base = base64.b64decode(link)
        file = f'/Users/proarea/Downloads/filetest{random.randint(0, 999)}.jpg'
        with open(file, 'wb+') as f:
            offset = link_base.find(b'\xff\xd8')
            f.write(link_base[offset:])
            check_file = os.path.exists(file)
            f.close()
        os.remove(file)
        return check_file

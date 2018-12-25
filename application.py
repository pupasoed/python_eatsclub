from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import pytest


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\python\\chromedriver.exe")
        self.driver.implicitly_wait(60)

    def open_home(self):
        self.driver.maximize_window()
        self.driver.get("https://eatsclub.dextechnology.com")

    def nav_linc(self, linc):
        driwer = self.driver
        self.driver.find_element_by_link_text(linc).click()

    def enter_email_and_pass(self, email, password):
        driver = self.driver
        # self.nav_linc("ВХОД")
        text_input = driver.find_elements_by_class_name('authorization__email-input')
        text_input[0].send_keys(email)
        text_input[1].send_keys(password, Keys.RETURN)
        time.sleep(1)
        autorization = driver.find_element_by_xpath("//input[@type='email']").get_attribute("value")
        assert autorization == email

    def destroy(self):
        self.driver.quit()

# Application = driver = open_hom_page()
# Application.login("vitia.88@mail.ru", "123456")
# time.sleep(2)
# driver.close()
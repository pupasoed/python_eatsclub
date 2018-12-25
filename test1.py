from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.firefox(executable_path="C:\\python\\geckodriver.exe")
driver.maximize_window()
driver.get("https://eatsclub.dextechnology.com")

def login (login, passw):
    driver.find_element_by_link_text("ВХОД").click()
    element = driver.find_element_by_link_text("ВХОД")
    # print(element.get_property('attributes')[0])
    email = driver.find_elements_by_class_name('authorization__email-input')
    email[0].send_keys(login)
    email[1].send_keys(passw)
    pass

login ('vitia.88@mail.ru', 123456)

autorization = driver.find_elements_by_xpath("/html/body/app-root/main/div/app-authorization/div/form/button")
autorization[0].click()

time.sleep(2)

driver.find_element_by_link_text("МАГАЗИН").click()
time.sleep(1)
program = driver.find_elements_by_class_name("short-product__item") # получили список программ питания
program[2].click()

time.sleep(10)
driver.close()
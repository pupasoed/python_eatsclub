from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\python\\chromedriver.exe")
driver.maximize_window()
driver.get("https://eatsclub.dextechnology.com")


def nav_linc(linc):
    driver.find_element_by_link_text(linc).click()

def login(login, passw):
    nav_linc("ВХОД")
    element = driver.find_element_by_link_text("ВХОД") # нашли все элементы формы логина
    # print(element.get_property('attributes')[0])  # вывести все атрибуты элементов переменной element
    email = driver.find_elements_by_class_name('authorization__email-input')
    email[0].send_keys(login)
    email[1].send_keys(passw, Keys.RETURN)
    print(driver.title)





    # email[1].send_keys(passw)
    # driver.find_element_by_css_selector("button[Text='ВОЙТИ']").click()

    # autorization = driver.find_elements_by_xpath("/html/body/app-root/main/div/app-authorization/div/form/button")
    # autorization[0].click()

    # formcontrol = driver.find_elements_by_css_selector('.form-control.ng-untouched.ng-pristine')
    # for i in formcontrol:
    #     print(i.get_property('attributes')[0])



login('vitia.88@mail.ru', '123456')
time.sleep(2)
# nav_linc("МАГАЗИН")
# time.sleep(1)
# program = driver.find_elements_by_class_name("short-product__item") # получили список программ питания
# program[2].click()
# time.sleep(2)



driver.close()
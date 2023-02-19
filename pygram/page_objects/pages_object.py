
from abc import ABC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from . import driver


# Responsável por definir os métodos da biblioteca do Selenium
class SeleniumMethods:
    def find_element_wait(locator, time=3, By=By.XPATH):
        try:
            return WebDriverWait(driver, time).until(
                EC.presence_of_element_located((By, locator))
            )
        except NoSuchElementException:
            return f'Elemento não encontrado na página\n Element: {locator}'

    def find_elements(locator):
        return driver.find_element(locator)

    def click(element):
        element.click()

    def send_keys(element, keys):
        element.send_keys(keys)

    def CLASSNAME():
        return By.CLASS_NAME

    def TAGNAME():
        return By.TAG_NAME

    def CSS():
        return By.CSS_SELECTOR


class Page(ABC, SeleniumMethods):
    def open(url=''):
        driver.get(url)


class PageElement(ABC, SeleniumMethods):
    def __init__(self):
        pass

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def type_text(self, locator, text):
        field = self.driver.find_element(*locator)
        field.send_keys(text)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500)")

    def wait_for_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element

    def take_screenshot(self, filename):
        filepath = f"screenshots/{filename}.png"
        self.driver.save_screenshot(filepath)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on element")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("JS Click")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Type text")
    def type_text(self, locator, text):
        field = self.driver.find_element(*locator)
        field.send_keys(text)

    @allure.step("Scrolling down")
    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500)")

    @allure.step("Waiting for element")
    def wait_for_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element

    @allure.step("Taking screenshot")
    def take_screenshot(self, filename):
        filepath = f"screenshots/{filename}.png"
        self.driver.save_screenshot(filepath)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=filename,
            attachment_type=allure.attachment_type.PNG
        )


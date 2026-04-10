from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[href="/directory"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-a-target="tw-input"]')
    KEEP_USING_WEB = (By.CSS_SELECTOR, 'button img[alt="Browser logo"]')
    ACCEPT_COOKIES = (By.CSS_SELECTOR,'[data-a-target="consent-banner-accept"]')

    @allure.step("Close popup")
    def close_popup(self):
        try:
            element = self.wait_for_element(self.KEEP_USING_WEB)
            self.js_click(element)
        except:
            pass

    @allure.step("Accept cookies")
    def accept_cookies(self):
        try:
            cookies = self.wait_for_element(self.ACCEPT_COOKIES)
            self.js_click(cookies)
        except:
            pass

    @allure.step("Search for game: {game_name}")
    def search_game(self, game_name):
        self.click_element(self.SEARCH_BUTTON)
        self.click_element(self.SEARCH_INPUT)
        self.type_text(self.SEARCH_INPUT, game_name + Keys.ENTER)


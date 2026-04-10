
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class SearchPage(BasePage):
    STREAMER_CARD = (By.CSS_SELECTOR, '.tw-channel-status-text-indicator')
    STREAMING_SCREEN = (By.CSS_SELECTOR, '[data-a-target="player-overlay-click-handler"]')
    VIDEO_PLAYER = (By.CSS_SELECTOR, 'video[aria-label="Twitch video player"]')

    @allure.step("Scrolling down twice")
    def scroll_down_twice(self):
        self.scroll_down()
        self.scroll_down()

    @allure.step("Get streamer card")
    def get_streamer_cards(self):
        stream_card = self.STREAMER_CARD
        all_cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(stream_card)
        )
        return all_cards

    @allure.step("Selecting streamer")
    def select_streamer(self):
        stream_cards = self.get_streamer_cards()
        first_card = stream_cards[0]
        self.js_click(first_card)

    @allure.step("Waiting for video is buffered")
    def wait_until_video_buffered(self, timeout=10):
        video = self.wait_for_element(self.VIDEO_PLAYER)

        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script(
                "return arguments[0].buffered.length > 0;", video
            )
        )
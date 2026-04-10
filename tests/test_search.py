from config import BASE_URL
from pages.main_page import MainPage
from pages.search_page import SearchPage


def test_search_game_shows_streamers(driver):
    driver.get(BASE_URL)
    main_page = MainPage(driver)
    main_page.close_popup()
    main_page.accept_cookies()
    main_page.search_game('StarCraft II')
    search_page = SearchPage(driver)
    search_page.scroll_down_twice()
    search_page.select_streamer()
    search_page.wait_until_video_buffered()
    search_page.take_screenshot("test_screen")


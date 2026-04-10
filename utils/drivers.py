from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    mobile_emulation = {"deviceName": "Pixel 7"}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    return driver
#  Twitch Selenium Framework

Automated UI test framework for Twitch web app using **Python + Selenium + pytest** with Chrome Mobile Emulation (Pixel 7).

![demo.gif](demo.gif)

---

##  Tech Stack

- Python 3.9
- Selenium WebDriver
- pytest
- Allure Reports
- Chrome Mobile Emulation (Pixel 7)
- Page Object Model (POM)

---

##  Project Structure

```
twitch-selenium-framework/
├── pages/
│   ├── base_page.py       # Base class with shared methods
│   ├── main_page.py       # Twitch main page (search, popups)
│   └── search_page.py     # Search results page
├── tests/
│   └── test_search.py     # Test cases
├── utils/
│   └── drivers.py         # Chrome driver factory
├── screenshots/           # Test screenshots
├── config.py              # Base URL and config
├── conftest.py            # pytest fixtures
└── requirements.txt
```

---

##  Test Cases

| # | Test | Description |
|---|------|-------------|
| 1 | `test_search_game_shows_streamers` | Search StarCraft II → scroll → select streamer → wait for video → screenshot |

---

##  How to Run

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run tests:**
```bash
pytest tests/ -v
```

**Run with Allure report:**
```bash
pytest tests/ -v --alluredir=allure-results
allure serve allure-results
```

---

##  Allure Report

Allure report includes all test steps with timing and screenshot attached.

---

##  Prerequisites

- Python 3.9+
- Google Chrome
- ChromeDriver
- Java (for Allure CLI)
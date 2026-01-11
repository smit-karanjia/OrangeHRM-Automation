import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import pytest_html

@pytest.fixture
def browserInstance():
    options = Options()
    options.add_argument("--start-maximized")

    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browserInstance")
        if not driver:
            return

        os.makedirs("reports/screenshots", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"reports/screenshots/{item.name}_{ts}.png"
        driver.save_screenshot(path)

        if hasattr(rep, "extra"):
            rep.extra.append(pytest_html.extras.image(path))

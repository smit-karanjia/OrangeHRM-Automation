from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HeaderPage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.user_menu = (By.CSS_SELECTOR, "span.oxd-userdropdown-tab")
        self.logout_btn = (By.XPATH, "//a[text()='Logout']")

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.user_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_btn)).click()

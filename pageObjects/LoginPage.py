from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.CSS_SELECTOR, "button[type='submit']")
        self.dashboard = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

        assert self.wait.until(EC.visibility_of_element_located(self.dashboard)), "Login failed"

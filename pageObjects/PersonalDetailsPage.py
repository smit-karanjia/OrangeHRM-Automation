from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.emp_id = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
        self.license = (By.XPATH, "//label[contains(text(),'License')]/following::input[1]")
        self.license_expiry = (By.XPATH, "//label[contains(text(),'Expiry')]/following::input[1]")
        self.nationality = (By.XPATH, "//label[text()='Nationality']/following::div[1]")
        self.marital = (By.XPATH, "//label[text()='Marital Status']/following::div[1]")
        self.dob = (By.XPATH, "//label[text()='Date of Birth']/following::input[1]")

        self.save_btn = (By.XPATH, "//button[normalize-space()='Save']")
        self.toast = (By.XPATH, "//p[contains(@class,'toast-message')]")
        self.loader = (By.CLASS_NAME, "oxd-loading-spinner")

    def wait_for_idle(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.loader))
        except:
            pass

    def get_emp_id(self):
        self.wait_for_idle()
        emp_id = self.wait.until(
            EC.visibility_of_element_located(self.emp_id)
        ).get_attribute("value")

        assert emp_id, "Employee ID not generated"
        return emp_id

    def set_text(self, locator, value):
        self.wait_for_idle()
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def set_date_direct(self, locator, value):
        self.wait_for_idle()
        field = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
            field,
            value
        )

    def select_dropdown(self, locator, value):
        self.wait_for_idle()
        self.wait.until(EC.element_to_be_clickable(locator)).click()

        options = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[@role='listbox']//span")
            )
        )

        for opt in options:
            if opt.text.strip() == value:
                opt.click()
                return

        raise AssertionError(f"Dropdown option '{value}' not found")

    def select_gender(self, gender):
        self.wait_for_idle()
        radio = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//label[text()='{gender}']")
            )
        )
        self.driver.execute_script("arguments[0].click();", radio)

    def save_details(self):
        self.wait_for_idle()
        save = self.wait.until(EC.element_to_be_clickable(self.save_btn))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save)
        self.driver.execute_script("arguments[0].click();", save)

        toast_msg = self.wait.until(
            EC.visibility_of_element_located(self.toast)
        ).text

        assert "Success" in toast_msg, "Personal details not saved"

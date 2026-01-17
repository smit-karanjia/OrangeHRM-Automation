from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.add_btn = (By.XPATH, "//button[normalize-space()='Add']")

        self.first_name = (By.NAME, "firstName")
        self.middle_name = (By.NAME, "middleName")
        self.last_name = (By.NAME, "lastName")

        self.login_toggle = (By.CSS_SELECTOR, "span.oxd-switch-input")
        self.username = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
        self.password = (By.XPATH, "//label[text()='Password']/../following-sibling::div/input")
        self.confirm_password = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input")

        self.save_btn = (By.XPATH, "//button[normalize-space()='Save']")

        self.emp_id_field = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")

        self.emp_id_search = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
        self.search_btn = (By.XPATH, "//button[normalize-space()='Search']")
        self.delete_icon = (By.XPATH, "//i[contains(@class,'bi-trash')]")
        self.confirm_delete = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
        self.no_records = (By.XPATH, "//span[text()='No Records Found']")

        self.loader = (By.CLASS_NAME, "oxd-loading-spinner")

    def wait_for_idle(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.loader))
        except:
            pass

    def add_employee(self, first, middle, last, username, password):
        self.wait.until(EC.element_to_be_clickable(self.pim_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_btn)).click()
        self.wait_for_idle()

        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(first)
        self.driver.find_element(*self.middle_name).send_keys(middle)
        self.driver.find_element(*self.last_name).send_keys(last)

        toggle = self.wait.until(EC.element_to_be_clickable(self.login_toggle))
        self.driver.execute_script("arguments[0].click();", toggle)
        self.wait_for_idle()

        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(password)

        save = self.wait.until(EC.element_to_be_clickable(self.save_btn))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save)
        self.wait_for_idle()
        self.driver.execute_script("arguments[0].click();", save)

        self.wait.until(EC.visibility_of_element_located(self.emp_id_field))

    def delete_employee(self, emp_id):
        self.wait.until(EC.element_to_be_clickable(self.pim_menu)).click()
        self.wait_for_idle()

        field = self.wait.until(EC.visibility_of_element_located(self.emp_id_search))
        field.clear()
        field.send_keys(emp_id)

        self.driver.find_element(*self.search_btn).click()
        self.wait_for_idle()

        self.wait.until(EC.element_to_be_clickable(self.delete_icon)).click()
        self.wait.until(EC.element_to_be_clickable(self.confirm_delete)).click()

        self.wait.until(EC.visibility_of_element_located(self.no_records))
        assert self.driver.find_element(*self.no_records).is_displayed(), "Employee was NOT deleted"

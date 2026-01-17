import json
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.PimPage import PimPage
from pageObjects.PersonalDetailsPage import PersonalDetailsPage
from pageObjects.HeaderPage import HeaderPage


with open("data/test_orangeFramework.json") as f:
    test_data = json.load(f)["data"]


@pytest.mark.parametrize("data", test_data)
def test_employee_lifecycle(browserInstance, data):
    driver = browserInstance

    # 1. Login as Admin
    LoginPage(driver).login(
        data["username1"],
        data["password1"]
    )

    # 2. Add Employee
    pim = PimPage(driver)
    pim.add_employee(
        data["firstname"],
        data["middlename"],
        data["lastname"],
        data["username2"],
        data["password2"]
    )

    # 3. Personal Details Page
    personal = PersonalDetailsPage(driver)

    emp_id = personal.get_emp_id()
    assert emp_id, "Employee ID not generated"

    personal.set_text(personal.license, data["dl_no"])
    personal.set_date_direct(personal.license_expiry, "2028-15-03")
    personal.select_dropdown(personal.nationality, data["nationality"])
    personal.select_dropdown(personal.marital, data["marital_status"])
    personal.set_date_direct(personal.dob, "1999-10-10")
    personal.select_gender(data["gender"])
    personal.save_details()

    # 4. Logout Admin
    HeaderPage(driver).logout()

    # 5. Login as New Employee
    LoginPage(driver).login(
        data["username2"],
        data["password2"]
    )

    HeaderPage(driver).logout()
    # 6. Login as Admin Again
    LoginPage(driver).login(
        data["username1"],
        data["password1"]
    )

    # 7. Delete Employee
    pim = PimPage(driver)
    pim.delete_employee(emp_id)

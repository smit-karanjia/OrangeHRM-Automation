#  OrangeHRM Web Application – Test Automation Framework

##  Project Overview
This project is a Selenium-based test automation framework developed to validate core HR workflows of the OrangeHRM web application.  

The objective of this project is to demonstrate practical Selenium automation skills aligned with real QA roles.

---

##  Scope of Automation
The automation suite covers the following key HR functionalities:

- Admin authentication and session validation
- Employee creation through the PIM module
- Personal details entry and data persistence
- User authentication using newly created employee credentials
- Role-based access verification (Admin vs Employee)
- Secure logout and session handling
- Employee deletion and data cleanup


---

##  Automated Test Flow

1. Login to OrangeHRM as an Admin user
2. Navigate to the PIM module and create a new employee
3. Redirect to the Personal Details page and save employee information
4. Logout from the Admin session
5. Login using the newly created employee credentials
6. Verify successful login and confirm the user is logged in as Employee (not Admin)
7. Logout from the employee session
8. Login again as Admin user
9. Locate and delete the created employee from the system
10. Confirm successful deletion to maintain test environment cleanliness

---

##  Framework Design & Architecture
The framework is designed for scalability and maintainability using the following principles:

- Page Object Model (POM) for separation of test logic and UI locators  
- Pytest framework for structured test execution  
- Reusable utility methods for browser actions and waits  
- Explicit waits to handle dynamic web elements  
- Modular and readable test cases for easy maintenance  

---

##  Tech Stack Used
- Programming Language: Python  
- Automation Tool: Selenium WebDriver  
- Test Framework: Pytest  
- Design Pattern: Page Object Model (POM)  
- Browser: Google Chrome  
- Version Control: Git & GitHub  

---

##  How to Run the Tests
1. Clone the repository  
2. Install required dependencies:
   pip install -r requirements.txt
3. Execute test using Pytest:
    pytest
4. Run tests with HTML report generation:
    pytest --html=reports/test_report.html --self-contained-html

---

##  Key Learnings & Outcomes
- Designed and developed a Selenium-based test automation framework from scratch using Python and Pytest
- Implemented the Page Object Model (POM) to improve maintainability and readability of UI automation tests
- Used explicit waits to handle dynamic web elements and reduce test flakiness
- Automated dependent workflows across multiple pages, including role-based login scenarios
- Improved debugging and test stability through structured test execution using Pytest

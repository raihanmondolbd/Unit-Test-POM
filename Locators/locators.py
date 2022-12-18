from selenium.webdriver.common.by import By


class Locators:
    userNameTextBox = (By.XPATH, '//input[@name="username"]')
    passWordTextBox = (By.XPATH, '//input[@name="password"]')
    submitButton = (By.XPATH, '//button[@type="submit"]')

    employeeList = (By.XPATH, '//a[contains(text(), "Employee List")]')
    performance = (By.XPATH, "(//a[@class='oxd-main-menu-item'])[6]")
    pim = (By.XPATH, '//a[@class="oxd-main-menu-item active"]')
    orangeImg = (By.XPATH, '//img[@alt="client brand banner"]')
    secondCheckbox = (By.XPATH, '(//div[@class="oxd-checkbox-wrapper"])[2]/label/input')
    secondCheckbox2 = (By.XPATH, '(//span[@class="oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input"])[2]')
    employee_id = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    select_dropdown = (By.XPATH, '//select')
    arg = (By.XPATH, '//option[@value="ARG"]')

    messageIcon = (By.XPATH, '//div[@class="sc-hMqMXs fHhYpP rsc-float-button react-draggable"]')
    nameTextBox = (By.XPATH, '//input[@placeholder="Name*"]')
    phoneNumberTextBox = (By.XPATH, '(//input[@class="sc-jAaTju bNMUeH"])[2]')
    messageTextArea = (By.XPATH, '//textarea[@type="textArea"]')
    addvertise = (By.XPATH, '//button[@class="bld-el   snp-close-link snp-cursor-pointer"]')
    iframe = (By.XPATH, '//iframe[@class="cwidsk16-styled-frame"]')
    chatClose = (By.XPATH, '//a[@class="sc-eNQAEJ kkgKxK rsc-header-close-button"]')
    searchTextbox = (By.XPATH, '(//input[@placeholder="Search for products"])[1]')
    searchIcon = (By.XPATH, '(//button[@class="searchsubmit"])[1]')
    googleSearchTextbox = (By.XPATH, '//input[@name="q"]')

class LoginPage():
    # Locators
    PROFILE_PAGE = "Profile Page"
    USER_INPUT = "tpt_loginUsername"
    PASS_INPUT = "tpt_loginPassword"
    WITHOUT_CV = 'methodButton--later'
    CONTINUE_BTN = 'Continue'
    PASS_CHOOSE = 'tpt_choosePassword'
    PASS_CONFIRM = 'tpt_chooseConfirmPassword'

    def __init__(self, driver):
        self.driver = driver

    # Acciones
    def login_in(self, username, password):
        login = self.driver.find_element_by_xpath("//a[contains(text(),'Login')]")
        login.click()
        username_input = self.driver.find_element_by_id(self.USER_INPUT)
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_id(self.PASS_INPUT)
        password_input.send_keys(password)

        login_btn = self.driver.find_element_by_xpath("//button[contains(text(),'Login')]")
        login_btn.click()

    def sign_in(self):
        apply_btn = self.driver.find_element_by_xpath("//a[contains(text(),'Apply')]")
        apply_btn.click()
        without_cv = self.driver.find_element_by_id(self.WITHOUT_CV)
        without_cv.click()
        first_name = self.driver.find_element_by_xpath("//input[preceding-sibling::label[text()='First name']]")
        first_name.send_keys("FirstName")
        last_name = self.driver.find_element_by_xpath("//input[preceding-sibling::label[text()='Last name']]")
        last_name.send_keys("LastName")
        mobile_num = self.driver.find_element_by_xpath("//input[preceding-sibling::label[text()='Mobile phone number']]")
        mobile_num.send_keys("12345678")
        mobile_num = self.driver.find_element_by_xpath("//input[preceding-sibling::label[text()='Email']]")
        mobile_num.send_keys("random+5@mail.com")
        acknowledge_checkbox = self.driver.find_element_by_id("209")
        acknowledge_checkbox.click()
        continue_btn = self.driver.find_element_by_xpath("//button[text()='"+str(self.CONTINUE_BTN)+"']")
        continue_btn.click()
        continue_btn = self.driver.find_element_by_xpath("//button[text()='" + str(self.CONTINUE_BTN) + "']")
        continue_btn.click()
        pass_create = self.driver.find_element_by_id(self.PASS_CHOOSE)
        pass_create.send_keys("Avature123")
        pass_confirm = self.driver.find_element_by_id(self.PASS_CONFIRM)
        pass_confirm.send_keys("Avature123")
        create_btn = self.driver.find_element_by_xpath("//button[contains(text(),'Create account')]")
        create_btn.click()

    def is_signin_successful(self):
        user_menu = self.driver.find_element_by_xpath("//a[contains(@class,'nav__item__link')]//img").is_displayed()
        return user_menu
    
    def is_login_successful(self):
        profile_title = self.driver.title
        return profile_title
    
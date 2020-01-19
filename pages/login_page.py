from base_page import BasePage, By


class LoginPage(BasePage):
    username_locator = (By.CSS_SELECTOR, '#username')
    password_locator = (By.CSS_SELECTOR, '#password_input')
    login_button = (By.CSS_SELECTOR, '#tcloud_login_button')

    def username_input_box(self):
        return self.find_element(self.username_locator)

    def password_input_box(self):
        return self.find_element(self.password_locator)

    def login_btn(self):
        return self.find_element(self.login_button)

class LoginPageAction(LoginPage):

    def login(self,username,password):
        self.username_input_box().clear()
        self.username_input_box().send_keys(username)
        self.password_input_box().clear()
        self.password_input_box().send_keys(password)
        self.login_btn().click()


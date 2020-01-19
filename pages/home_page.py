from base_page import BasePage, By

class HomePage(BasePage):

    user_title_locator =(By.CSS_SELECTOR,'.avatar-text-default.avatar-Q')

    def user_title(self):
        return self.find_element(self.user_title_locator)

class HomePageAction(HomePage):

    @property
    def get_user_title(self):
        return self.user_title().get_attribute('title')
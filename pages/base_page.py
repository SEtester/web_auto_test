from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.tapd.cn/'
LOGIN_URL = '/cloud_logins/login'
TIMEOUT = 10
POLL_FREQUENCY = 0.5


class BasePage():

    def __init__(self, driver=None, path=None):
        self.driver = driver if driver != None else webdriver.Chrome()
        self.get_url(path)

    def find_element(self, locator):
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_url(self, path=None):
        if path != None:
            url = URL + path
        else:
            url = None

        if url != None:
            self.driver.get(url)


if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    # 构造base_page对象，同时打开目的页面
    base_page = BasePage(path=LOGIN_URL)
    login_locator = (By.CSS_SELECTOR, '#username')
    base_page.find_element(login_locator).send_keys('123456')
    input()
    base_page.driver.quit()
    base_page.driver = None

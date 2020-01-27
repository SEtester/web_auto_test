import sys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.constants import TIMEOUT, POLL_FREQUENCY, DOMAIN
from utils.se_utils import Driver
from utils.log_utils import GetLogger

logger = GetLogger.get_logger()


class BasePage():

    def __init__(self, path=None):
        self.driver = Driver.get_driver()
        self.driver.maximize_window()
        self.get_url(path)

    def find_element(self, locator):
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_url(self, path=None):

        if path != None:

            try:
                domain = DOMAIN[sys.argv[-1]]
            except Exception as e:
                logger.info('找不到环境变量,设置环境变量为默认的url:{}'.format(DOMAIN['test']))
                domain = DOMAIN['test']

            url = domain + path
        else:
            url = None

        if url != None:
            self.driver.get(url)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()


if __name__ == '__main__':
    from selenium.webdriver.common.by import By
    from utils.constants import LOGIN_URL

    # 构造base_page对象，同时打开目的页面
    base_page = BasePage(path=LOGIN_URL)
    login_locator = (By.CSS_SELECTOR, '#username')
    base_page.find_element(login_locator).send_keys('123456')
    input()
    base_page.driver.quit()
    # base_page.driver = None

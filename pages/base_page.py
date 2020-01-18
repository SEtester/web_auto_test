from selenium import webdriver

URL = 'https://www.tapd.cn/'
LOGIN_URL = '/cloud_logins/login'

class BasePage():

    def __init__(self, driver=None, path=None):
        self.driver = driver if driver != None else webdriver.Chrome()
        self.get_url(path)

    def find_element(self):
        pass

    def get_url(self, path=None):
        if path != None:
            url = URL + path
        else:
            url = None

        if url != None:
            self.driver.get(url)


if __name__ == '__main__':
    # 构造base_page对象，同时打开目的页面
    base_page = BasePage(path=LOGIN_URL)

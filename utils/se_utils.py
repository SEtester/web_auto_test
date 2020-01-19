from selenium import webdriver


class DriverUtil():
    _driver = None

    @classmethod
    def get_driver(cls, browser_name='Chrome'):
        if cls._driver == None:
            if browser_name == 'Chrome':
                cls._driver = webdriver.Chrome()
            elif browser_name == 'Firefox':
                cls._driver = webdriver.Firefox()
            elif browser_name == 'Safari':
                cls._driver == webdriver.Safari()
            elif browser_name == 'Opera':
                cls._driver == webdriver.Opera()
            elif browser_name == 'edge':
                cls._driver == webdriver.Edge()
            elif browser_name == 'Ie':
                cls._driver == webdriver.Ie()
            else:
                raise NameError(
                    "Not found %s browser,You can enter 'Chrome', 'Firefox', 'Ie', 'Edge', 'Safari',Opera" % browser_name)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None

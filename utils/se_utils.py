from selenium import webdriver

from utils.log_utils import GetLogger

logger = GetLogger.get_logger()

class Driver():
    _driver = None

    @classmethod
    def get_driver(cls, browser_name='Chrome'):
        if cls._driver == None:
            logger.info('正在打开浏览器.....')
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
            logger.info('打开{}浏览器'.format(cls._driver.name))

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            logger.info('正在关闭{}浏览器'.format(cls._driver.name))
            cls._driver.quit()
            logger.info('已关闭{}浏览器'.format(cls._driver.name))

        cls._driver = None

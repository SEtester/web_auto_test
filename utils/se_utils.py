from selenium import webdriver


class DriverUtil():

    _driver = None


    @classmethod
    def get_driver(cls,browser_name='chrome'):
        if cls._driver == None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()



    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None

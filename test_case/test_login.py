import unittest

from pages.login_page import LoginPageAction
from utils.constants import LOGIN_URL


class TestLoginCase(unittest.TestCase):


    def test_login_success_with_email(self):
        username = 'XXXXXX'
        password = 'XXXXXX'
        login_page = LoginPageAction(path=LOGIN_URL)
        home_page = login_page.login(username=username, password=password)
        user_title = home_page.get_user_title
        expect_ret = 'XXXXXX'
        self.assertEqual(expect_ret, user_title)

    def test_login_success_with_mobile_phone(self):
        username = 'XXXXXX'
        password = 'XXXXXX'
        login_page = LoginPageAction(path=LOGIN_URL)
        home_page = login_page.login(username=username, password=password)
        user_title = home_page.get_user_title
        expect_ret = 'XXXXXX'
        self.assertEqual(expect_ret, user_title)


if __name__ == '__main__':
    unittest.main()

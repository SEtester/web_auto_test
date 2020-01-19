import unittest
from test_case.test_login import TestLoginCase
from utils.se_utils import Driver

if __name__ == '__main__':
    cases = unittest.TestLoader().loadTestsFromTestCase(TestLoginCase)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(cases)

    # 所有用例运行完后关闭浏览器
    Driver.quit_driver()

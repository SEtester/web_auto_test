import unittest

from module_path import *
from test_case.test_login import TestLoginCase
from utils.se_utils import Driver
from utils.HTMLTestRunnerChart import HTMLTestRunner

if __name__ == '__main__':
    cases = unittest.TestLoader().loadTestsFromTestCase(TestLoginCase)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(cases)

    runner = HTMLTestRunner(
        title="带截图，饼图，折线图，历史结果查看的测试报告",
        description="",
        stream=open(report_path, "wb"),
        verbosity=2,
        retry=0,
        save_last_try=True)
    runner.run(cases)
    # 所有用例运行完后关闭浏览器
    Driver.quit_driver()
    Driver.Driver = None

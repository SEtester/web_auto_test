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
        title="自动化测试报告",
        description="%s ,%s"%(Driver.get_driver().name,cul_platform),
        stream=open(report_path, "wb"),
        verbosity=2,
        retry=0,
        save_last_try=True)
    runner.run(cases)
    # 所有用例运行完后关闭浏览器
    Driver.quit_driver()
    Driver.Driver = None

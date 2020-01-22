import unittest
import configparser

from module_path import *
from test_case.test_login import TestLoginCase
from utils.se_utils import Driver
from utils.HTMLTestRunnerChart import HTMLTestRunner
from utils.mail_utils import send_mail

if __name__ == '__main__':
    ###### 执行测试用例 ######
    cases = unittest.TestLoader().loadTestsFromTestCase(TestLoginCase)
    runner = HTMLTestRunner(
        title="自动化测试报告",
        description="%s ,%s" % (Driver.get_driver().name, cul_platform),
        stream=open(report_path, "wb"),
        verbosity=2,
        retry=0,
        save_last_try=True)
    runner.run(cases)

    # 所有用例运行完后关闭浏览器
    Driver.quit_driver()


    ###### 邮件发送 ######
    config = configparser.ConfigParser()
    config.read(mail_config_path)
    project_member = config.items('project_member')

    subject = 'Web Ui 自动化测试报告'
    body = '正文内容'
    to = project_member_list = [x[1] for x in project_member]
    html = open(report_path, 'r', encoding='utf-8').read()
    file = report_path
    send_mail(to=to, subject=subject,
              contents=[file])

import os
import sys
import time

web_auto_test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages_dir_path = web_auto_test_path + '/pages'
config_dir_path = web_auto_test_path + '/config'
run_case_dir_path = web_auto_test_path + '/run_case'
test_case_dir_path = web_auto_test_path + '/test_case'
utils_dir_path = web_auto_test_path + '/utils'
report_dir_path = web_auto_test_path + '/report'



sys.path.extend([
    web_auto_test_path,
    pages_dir_path,
    config_dir_path,
    run_case_dir_path,
    test_case_dir_path,
    utils_dir_path,
])

from pprint import pprint

print('python引包路径:')
pprint(sys.path)

report_name = time.strftime('%Y%m%d%H%M%S') + 'WebUiTest' + '.html'
report_path = report_dir_path + '/' + report_name

# 操作系统名称
cul_platform = sys.platform
print(cul_platform)
import os
import sys

web_auto_test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages_dir_path = web_auto_test_path + '/pages'
config_dir_path = web_auto_test_path + '/config'
run_case_dir_path = web_auto_test_path + '/run_case'
test_case_dir_path = web_auto_test_path + '/test_case'
utils_dir_path = web_auto_test_path + '/utils'

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

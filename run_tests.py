import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
sys.path.append('./HTMLTestRunner_PY3')
# from HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
import HtmlTestRunner
import unittest
from db_fixture import test_data


test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    test_data.init_data()

    # now = time.strftime(r"%Y-%m-%d %H_%M_%S")
    # filename = './reports/' + now + '_result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='Guest Manage Interface Test', description='Implementation Example with:')
    # runner.run(discover)
    # fp.close()

    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir', report_title='Guest Manage Interface Test'))
    runner = HtmlTestRunner.HTMLTestRunner(output='', report_title='Guest Manage Interface Test')
    runner.run(discover)
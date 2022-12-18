import unittest

from TestCases.test_dropdown import Dropdown
from TestCases.test_iframe import IframeTest
from TestCases.test_login import LoginTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(IframeTest('test_iframe'))
    suite.addTest(LoginTest('test_login'))
    suite.addTest(Dropdown('test_dropdown'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

import unittest
import HtmlTestRunner

from tests.login_new_user import TestBebeTeiLoginNewUser
from tests.login_registered_user_positive import TestBebeTeiLoginRegisteredUserPositive
from tests.cart_test import BebeTeiCart


class TestSuite(unittest.TestCase):
    # Import test modules

    def test_suite(self):
        # create a test suite
        suite = unittest.TestSuite()

        # add tests to test suite
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestBebeTeiLoginNewUser))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestBebeTeiLoginRegisteredUserPositive))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(BebeTeiCart))

        # set up the HTMLTestRunner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            # write the right version of the app under test Preproduction/QA /ETC
            report_title='BebeTei website testing',
            report_name='Test Result'
        )

        # run the test suite
        runner.run(suite)

if __name__ == "__main__":
    unittest.main()
import unittest

from selenium_utils import open_dash

# https://github.com/otron/flask-travis-selenium-minimality/blob/master/tests/seltest.py

class Test_app(unittest.TestCase):

    driver = open_dash()

    def test_title(self):

        self.assertEqual("Dash", self.driver.title)



if __name__ == '__main__':
    unittest.main()

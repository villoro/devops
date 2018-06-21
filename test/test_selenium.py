import unittest

from src.utils import open_dash


class Test_app(unittest.TestCase):

    driver = open_dash()

    def test_title(self):

        self.assertEqual("Dash", self.driver.title)



if __name__ == '__main__':
    unittest.main()

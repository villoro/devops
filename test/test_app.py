""" Tests the dash app """
import unittest

from src import index

class TestApp(unittest.TestCase):
    """ Tests the dash app """

    def test_values(self):
        """ Test the list of values in index """
        self.assertEqual(index.VAUES, ['MTL', 'BCN'])

    def test_server(self):
        """ Test that there is a server in index """
        self.assertIsNotNone(index.SERVER)



if __name__ == '__main__':
    unittest.main()

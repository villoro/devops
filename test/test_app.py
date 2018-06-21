import unittest

from src import index

class Test_app(unittest.TestCase):

    def test_values(self):
        self.assertEqual(index.VAUES, ['MTL', 'BCN'])

    def test_server(self):
        self.assertIsNotNone(index.SERVER)



if __name__ == '__main__':
    unittest.main()

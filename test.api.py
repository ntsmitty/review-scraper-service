import unittest

from api import app

class TestGetAPI(unittest.TestCase):

    def test_response(self):
        tester = app.test_client(self)
        response = tester.get('/reviews')
        self.assertEqual(response.status_code, 200)    


if __name__ == '__main__':
    unittest.main()
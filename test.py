import app as flask_app

import unittest

class testing_flask(unittest.TestCase):

    def setup(self):
        self.app = flask_app.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response =  self.app.get('/')
        self.assertEqual(response, 200)

    def test_message(self):
        greeting = {'talha':'something'}
        self.assertDictEqual(flask_app.start(), greeting)

if __name__ == '__main__':
    unittest.main()


import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_event/'
        self.result = None
    
    def tearDown(self):
        print(self.result)
    
    def test_add_event_all_null(self):
        payload = {
            'eid': '',
            '': '',
            'attendees_limit': '',
            'address': '',
            'start_time': ''
        }
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')


if __name__ == '__main__':
    test_data.init_data()
    unittest.main()


    
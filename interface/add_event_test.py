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

    def test_add_event_name_exist(self):
        payload = {
            'eid': 1,
            'name': '小米Note手机发布会',
            'attendees_limit': 200,
            'status': 1,
            'address': '北京798艺术区c区1号',
            'start_time': '2018-7-11 09:30:00',
            # 'create_time': '2018-4-11 09:30:00'
        }
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_data_type_error(self):
        payload = {
            'eid': 8,
            'name': '锤子科技T9手机发布会',
            'attendees_limit': 100,
            'status': 1,
            'address': '北京航空航天大学东区报告厅',
            'start_time': '2014-8-12',
            # 'create_time': '2013-2-11 09:30:00'
        }
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error', self.result['message'])

    def test_add_event_success(self):
        payload = {
            'eid': 20,
            'name': '锤子科技TNT效率工具发布会',
            'attendees_limit': 100,
            'status': 1,
            'address': '北京航空航天大学东区报告厅',
            'start_time': '2019-2-11 09:30:00',
            # 'create_time': '2013-2-11 09:30:00'
        }
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    test_data.init_data()
    unittest.main()


    
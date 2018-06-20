import unittest, requests, hashlib
from time import time


class AddEventWithAuthTest(unittest.TestCase):
    """
    Test adding event with auth
    """

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/sec_add_event/'
        self.api_key = '2018FIFAWorldCup'
        now_time = time()
        self.client_time = str(now_time).split('.')[0]
        
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()
    
    def test_add_event_request_error(self):
        """
        request method error
        """
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'request error')

    def test_add_event_sign_null(self):
        """
        signature is null
        """
        payload = {
            'eid': 1,
            '': '',
            'attendees_limit': '',
            'address': '',
            'start_time': '',
            'time': '',
            'sign': ''
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user sign null')
    
    def test_add_event_time_out(self):
        """
        request timeout(>60s)
        """
        now_time = str(int(self.client_time) - 61)
        payload = {
            'eid': 1,
            '': '',
            'attendees_limit': '',
            'address': '',
            'start_time': '',
            'time': now_time,
            'sign': 'sign-null'
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10013)
        self.assertEqual(result['message'], 'user sign timeout')
    
    def test_add_event_sign_error(self):
        """
        signature error
        """
        payload = {
            'eid': 1,
            '': '',
            'attendees_limit': '',
            'address': '',
            'start_time': '',
            'time': self.client_time,
            'sign': 'incorrect-sign-str'
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10014)
        self.assertEqual(result['message'], 'user sign error')

    def test_add_event_success(self):
        """
        general positive case
        """
        payload = {
            'eid': 12,
            'name': '锤子科技未来手机X1发布会',
            'attendees_limit': '5000',
            'address': '人民大会堂',
            'start_time': '2020-05-02 12:12:00',
            'time': self.client_time,
            'sign': self.sign_md5
        }
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'add event success')


if __name__ == '__main__':
    unittest.main()

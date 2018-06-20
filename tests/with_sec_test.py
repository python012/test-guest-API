import unittest
import requests


class GetEventListTest(unittest.TestCase):
    '''Get event list, request with auth'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/sec_get_event_list/'

    def test_get_event_list_auth_null(self):
        '''Auth field is null'''
        r = requests.get(self.base_url, params={'eid':1})
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'user auth null')
    
    def test_get_event_list_auth_error(self):
        '''Auth infor error'''
        auth_user = ('abc', '123')
        r = requests.get(self.base_url, auth=auth_user, params={'eid':1})
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user auth fail')
    
    def test_get_event_list_eid_null(self):
        '''eid is null'''
        auth_user = ('admin', 'admin01234')
        r = requests.get(self.base_url, auth=auth_user, params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')
    
    def test_get_list_eid_success(self):
        '''general postive case'''
        auth_user = ('admin', 'admin01234')
        r = requests.get(self.base_url, auth=auth_user, params={'eid':'1'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(len(result['data']), 1)
        self.assertEqual(result['data'][0]['name'], u'小米Note手机发布会')
        self.assertEqual(result['data'][0]['address'], u'北京798艺术区c区1号')


if __name__ == '__main__':
    unittest.main()

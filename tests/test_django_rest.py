import unittest, requests


class UserTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users'
        self.auth = ('admin', 'admin01234')
    
    def test_user1(self):
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'admin')
        self.assertEqual(result['email'], 'admin@u.com')
    
    def test_user2(self):
        r = requests.get(self.base_url + '/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'jack')
        self.assertEqual(result['email'], 'jack@mail.com')

    def test_user3(self):
        r = requests.get(self.base_url + '/3/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'tom')
        self.assertEqual(result['email'], 'tom@mail.com')


class GroupTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('admin', 'admin01234')
    
    def test_group1(self):
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'test')
    
    def test_group2(self):
        r = requests.get(self.base_url + '/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'developer')


if __name__ == '__main__':
    unittest.main()

import sys
sys.path.append('../db_fixture')
from db_fixture.mysql_db import DB
from faker import Faker
from random import randrange


_fake = Faker('zh_CN')

def _create_fake_guest(id, event_id_range):
    fake_guest = {}
    fake_guest['id'] = id
    fake_guest['realname'] = _fake.name()
    fake_guest['phone'] = _fake.phone_number()
    fake_guest['email'] = _fake.free_email()
    fake_guest['sign'] = 0
    fake_guest['event_id'] = randrange(1, event_id_range)
    fake_guest['create_time'] = '2018-6-11 09:30:00'
    return fake_guest

_fake_guest_list = []

for id in range(1, 500):
    _fake_guest_list.append(_create_fake_guest(id, 7))

datas = {
    'sign_event':[
        {
            'id': 1,
            'name': '小米Note手机发布会',
            'attendees_limit': 200,
            'status': 1,
            'address': '北京798艺术区c区1号',
            'start_time': '2018-7-11 09:30:00',
            'create_time': '2018-4-11 09:30:00'
        },
        {
            'id': 2,
            'name': '锤子科技R1手机发布会',
            'attendees_limit': 300,
            'status': 1,
            'address': '北京国家体育场鸟巢',
            'start_time': '2018-5-11 09:30:00',
            'create_time': '2018-2-11 09:30:00'
        },
        {
            'id': 3,
            'name': 'Vivo P1手机发布会',
            'attendees_limit': 300,
            'status': 1,
            'address': '深圳华强北9号楼1层',
            'start_time': '2018-9-11 09:30:00',
            'create_time': '2018-3-11 09:30:00'
        },
        {
            'id': 4,
            'name': 'iPhone X1手机发布会',
            'attendees_limit': 3020,
            'status': 1,
            'address': '帕拉奥图芳草地艺术活动中心',
            'start_time': '2019-5-11 09:30:00',
            'create_time': '2018-2-11 09:30:00'
        },
        {
            'id': 5,
            'name': '华为荣耀P10手机发布会',
            'attendees_limit': 3900,
            'status': 1,
            'address': '深圳华为坂田研发中心9号食堂大厅',
            'start_time': '2018-10-11 09:30:00',
            'create_time': '2018-2-11 09:30:00'
        },
        {
            'id': 6,
            'name': '华为Note 2手机发布会',
            'attendees_limit': 3300,
            'status': 1,
            'address': '深圳华为坂田研发中心9号食堂大厅',
            'start_time': '2018-12-1 09:30:00',
            'create_time': '2018-2-11 09:30:00'
        },
        {
            'id': 7,
            'name': '锤子科技T1手机发布会',
            'attendees_limit': 100,
            'status': 1,
            'address': '北京航空航天大学东区报告厅',
            'start_time': '2014-8-1 09:30:00',
            'create_time': '2013-2-11 09:30:00'
        },
    ],
    'sign_guest':_fake_guest_list,
}


def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()

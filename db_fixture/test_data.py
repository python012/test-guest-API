import sys
sys.path.append('../db_fixture')
from mysql_db import DB


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
    ],
    'sign_guest':[
        {
            'id': 1,
            'realname': 'John',
            'phone': '01020122',
            'email': 'john@ui.com',
            'sign': '0',
            'event_id': 1,
            'create_time': '2018-6-11 09:30:00',
        }, 
        {
            'id': 2,
            'realname': 'Alex',
            'phone': '9220122',
            'email': 'alex@ui.com',
            'sign': '0',
            'event_id': 2,
            'create_time': '2018-6-11 09:30:00',
        }, 
        {
            'id': 3,
            'realname': 'Jane',
            'phone': '00982092',
            'email': 'jane@ui.com',
            'sign': '0',
            'event_id': 3,
            'create_time': '2018-6-11 09:30:00',
        }, 
        {
            'id': 4,
            'realname': 'Wong',
            'phone': '11902',
            'email': 'won@ui.com',
            'sign': '0',
            'event_id': 4,
            'create_time': '2018-6-11 09:30:00',
        }, 
    ],
}

def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
        # db.close() # Pending issue: will raise pymysql.err.InterfaceError: (0, '')


if __name__ == '__main__':
    init_data()
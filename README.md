# test-guest-API

## SETUP

### Option 1

Do it manually, just use MySql to setup database and tables:

``` sql
create database guest_test;
use guest_test;
CREATE TABLE sign_event(id INT PRIMARY KEY, name VARCHAR(100), attendees_limit INT, status BOOLEAN, address VARCHAR(200), start_time DATETIME) DEFAULT CHARSET=utf8;
```

### Option 2

Create database guest_test in MySql, rename the database name in `guest/settings.py` of guest project folder, and run `python3 manage.py runserver`, Django will help init the tables structure.

## TEST

Run `db_fixture/mysql_db.py` and the following is expected:

``` text
mysql> select * from sign_event;
+----+-----------+-----------------+--------+-------------------------------------------+---------------------+
| id | name      | attendees_limit | status | address                                   | start_time          |
+----+-----------+-----------------+--------+-------------------------------------------+---------------------+
| 12 | 大可乐    |             200 |      1 | 古城大理南陵西路12号悦来客栈              | 2012-09-12 14:30:00 |
+----+-----------+-----------------+--------+-------------------------------------------+---------------------+
1 row in set (0.00 sec)
```

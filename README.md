# test-guest-API

## SETUP

Use MySql to setup database:

``` sql
create database guest_test;
use guest_test;
CREATE TABLE sign_event(id INT PRIMARY KEY, name VARCHAR(100), attendees_limit INT, status BOOLEAN, address VARCHAR(200), start_time DATETIME) DEFAULT CHARSET=utf8;
```

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
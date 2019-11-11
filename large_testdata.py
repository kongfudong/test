# -*- coding: utf-8 -*-
import pymysql
from faker import Faker

conn = pymysql.connect(host="10.167.196.158", port=3306, user="nbi", password="Nbi@1234", charset="utf8")

database_sql ="""CREATE DATABASE if not exists test CHARACTER SET utf8 COLLATE utf8_general_ci;"""

cursor = conn.cursor()
cursor.execute(database_sql)
cursor.execute('use test;')
# 这里给出表结构，如果使用已存在的表，可以不创建表。
sql = """
create table if not exists user(
id int PRIMARY KEY auto_increment,
username VARCHAR(20),
password VARCHAR(20),
address VARCHAR(35) 
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
fake = Faker("zh-CN")
for i in range(20):
    sql = """insert into user(username,password,address) 
    values('%s','%s','%s')""" \
          % (fake.city(), fake.password(special_chars=False), fake.address())
    cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()

#!/user/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
from sshtunnel import SSHTunnelForwarder

# sms_verification_codes 查询
def mysql_query_codes(cellphone):
    conn = MySQLdb.connect(host='10.1.11.51',  # 此处必须是是127.0.0.1
                           port=3306,
                           user='root',
                           passwd='lianqian123',
                           db='lqmall_db')
    cursor = conn.cursor()
    sql = "SELECT * from sms_verification_codes where svc_cellphone=" + cellphone
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print row
    except:
        # conn.rollback()
        print "query error"
    conn.close()

# kld_caifu_wealth.users 查询
def mysql_query_users(cellphone):
    with SSHTunnelForwarder(
            ssh_address_or_host=('118.31.70.164', 9998),
            ssh_username='0f678e_root',
            ssh_password='Yfb111qqq',
            remote_bind_address=('rm-bp15w7k0q227b34tu.mysql.rds.aliyuncs.com', 3306)) as server:
        conn = MySQLdb.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                               port=server.local_bind_port,
                               user='kld',
                               passwd='Kld123456')
        cursor = conn.cursor()
        sql = "select * from kld_caifu_wealth.users where cellphone=" + cellphone
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print row
        except:
            # conn.rollback()
            print "query error"
        conn.close()
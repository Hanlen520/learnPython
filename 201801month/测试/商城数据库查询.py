#!/user/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import csv
from sshtunnel import SSHTunnelForwarder

class QueryShopInfo():
    def __init__(self,conn):
        self.conn = conn

    # sms_verification_codes 查询手机号的验证码(商城)
    def query_vericodes(self,cellphone):
        vericodes=[]
        cursor = self.conn.cursor()
        sql = "SELECT * from lqmall_db.sms_verification_codes where svc_cellphone=" + cellphone
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                vericodes.append(row[3])
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        finally:
            cursor.close()
        return vericodes

    # userIdentifier
    def query_userinfo(self,cellphone):
        userIdentifier=[]
        cursor = self.conn.cursor()
        sql = "select * from kld_caifu_wealth.users where cellphone=" + cellphone
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                userIdentifier.append(row[1])
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        finally:
            cursor.close()
        return userIdentifier

if __name__ == '__main__':
    cellphone = '13572489850'
    # 数据库连接
    with SSHTunnelForwarder(
            ssh_address_or_host=('118.31.70.164', 9998),
            ssh_username='0f678e_root',
            ssh_password='Yfb111qqq',
            remote_bind_address=('rm-bp15w7k0q227b34tu.mysql.rds.aliyuncs.com', 3306)) as server:
        conn = MySQLdb.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                               port=server.local_bind_port,
                               user='kld',
                               passwd='Kld123456')
        with conn:
            mysql_shop = QueryShopInfo(conn)
            vericodes = mysql_shop.query_vericodes(cellphone)
            print cellphone,u" 验证码: ",vericodes

            userIdentifier = mysql_shop.query_userinfo(cellphone)
            print cellphone, u" userIdentifier: ", userIdentifier


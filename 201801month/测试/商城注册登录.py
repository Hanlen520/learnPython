#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
from Crypto.Cipher import AES
import base64,json
import hashlib
import MySQLdb
from sshtunnel import SSHTunnelForwarder

PADDING = '\0'
# pkcs5padding
pad_it = lambda s: s+(16 - len(s)%16)*chr(16 - len(s) % 16)
URL_SHOP = "http://10.1.11.51:8080"

cellphone = '15800876020'

def encrypt(pswStr):
    generator = AES.new('kaledaimall98765', AES.MODE_CBC, 'kaledaimall98765')
    crypt = generator.encrypt(pad_it(pswStr))
    cryptedStr = base64.b64encode(crypt)
    return cryptedStr

def md5(str):
    md5_pwd = hashlib.md5()
    # 158 9544b351297a40b18cb5252eb7cdedd60 0876019
    md5_pwd.update(str)
    print u"sign加密后：",md5_pwd.hexdigest()
    return md5_pwd.hexdigest()

def sendVeriCodes():
    url = URL_SHOP + '/lqmall/veriCodes/sendVeriCodes'
    data = {
        'cellphone': cellphone,
        'type':2,
        # 手机前3位+salt+手机后8位，得到的结果再MD5一下
        'sign': md5(cellphone[:3] + "9544b351297a40b18cb5252eb7cdedd6" + cellphone[3:])
    }
    # 以json形式发送post请求
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    if response.status_code == 200:
        print response.content

def validVeriCodes():
    url = URL_SHOP + '/lqmall/veriCodes/validVeriCodes'
    data = {
        'cellphone': cellphone,
        'type':2,
        'code':832647
    }
    # 以json形式发送post请求
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    identifier = ""
    if response.status_code == 200:
        print response.content
        identifier = response.json()['identifier']
    return identifier

def signUp(identifier):
    url = URL_SHOP + '/lqmall/user/signUp'
    data = {
        'cellphone': cellphone,
        'identifier':identifier,
        'password': encrypt('456456')
    }
    # 以json形式发送post请求
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    if response.status_code == 200:
        print response.content

def isregister():
    url = URL_SHOP + '/lqmall/isregister'
    params = {
        'cellphone': cellphone
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        print response.content

# sms_verification_codes 查询
def mysql_query_codes():
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
def mysql_query_users():
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

if __name__ == '__main__':
    # 1.发送短信
    # sendVeriCodes()

    mysql_query_codes()

    # 2.验证短信
    # identifier = validVeriCodes()
    # 注册
    # signUp(identifier)

    # isregister()

    mysql_query_users()

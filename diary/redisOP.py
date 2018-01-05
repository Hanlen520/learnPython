#!/user/bin/env python
# -*- coding:utf-8 -*-

#导入我们需要用到的包和类并且起别名
import redis

def main():
    print "Start"
    # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    # r = redis.Redis(host='47.96.171.4', port=6379, password="0987654321rfvujmtgbyhn")
    r = redis.Redis(host='120.55.42.27', port=6379, password="123456")
    print r.get('zhima_credit_key')
    print r.delete('zhima_credit_key')

if __name__ == '__main__':  
    main()  
#!/user/bin/env python
# -*- coding:utf-8 -*-
import redis
import configparser

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='47.96.171.4',password='0987654321rfvujmtgbyhn', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    config = configparser.ConfigParser()
#!/user/bin/env python
# -*- coding:utf-8 -*-
import paramiko

# SFTPClient用于连接远程服务器并进行上传下载功能。
def downfromserver(hostname, port, username, password):
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)

    srcPath = ""
    desPatn ="E:\\log"
    # 将remove_path 下载到本地 local_path
    sftp.get('/home/www/tomcat_web/logs/catalina.out', 'E:\\log\\catalina.out')

    transport.close()

if __name__ == '__main__':
    downfromserver('118.31.70.164', 9998, '3602d0_root', 'Yfb111qqq')
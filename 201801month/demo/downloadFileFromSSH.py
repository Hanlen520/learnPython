#!/user/bin/env python
# -*- coding:utf-8 -*-
import paramiko

def connect(hostname,port,username,password):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname,port=port,username=username,password=password)

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('cd /home/www/tomcat_web/logs\n ls')
    # 获取命令结果
    print stdout.read()
    ssh.close()

# SFTPClient用于连接远程服务器并进行上传下载功能。
def downfromserver(hostname, port, username, password):
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将location.py 上传至服务器 /tmp/test.py
    # sftp.put('/tmp/location.py', '/tmp/test.py')
    # 将remove_path 下载到本地 local_path
    sftp.get('/home/www/tomcat_web/logs/catalina.out', 'F:\\test\\catalina.out')

    transport.close()

if __name__ == '__main__':
    connect('118.31.70.164',9998,'3602d0_root','Yfb111qqq')
    downfromserver('118.31.70.164',9998,'3602d0_root','Yfb111qqq')
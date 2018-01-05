#!/user/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
from sshtunnel import SSHTunnelForwarder
import paramiko

def connection():
	with SSHTunnelForwarder(
			('118.31.70.164', 9998),  # B机器的配置
			ssh_password="52aab2_root",
			ssh_username="Yfb111qqq",
			remote_bind_address=('120.55.42.27', 3306)) as server:  # A机器的配置

		conn = MySQLdb.connect(host='120.55.42.27',  # 此处必须是是127.0.0.1
							   port=server.local_bind_port,
							   user='kld',
							   passwd='Kld123456',
							   db='kld_caifu_wealth')
def connection2():
	with SSHTunnelForwarder(
			('47.96.183.61', 22),  # B机器的配置
			ssh_password="root",
			ssh_username="R360111qqq",
			remote_bind_address=('rm-bp13gy0jb0vzg1drm.mysql.rds.aliyuncs.com', 3306)) as server:  # A机器的配置

		conn = MySQLdb.connect(host='rm-bp13gy0jb0vzg1drm.mysql.rds.aliyuncs.com',  # 此处必须是是127.0.0.1
							   port=server.local_bind_port,
							   user='lqmall',
							   passwd='hzDz2SZhkwhU1Zmy')

def connection3():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("47.96.183.61", 22, "root", "R360111qqq")
	stdin, stdout, stderr = ssh.exec_command("mysql -ulqmall -phzDz2SZhkwhU1Zmy -Dlqmall_db -e 'select ui_cellphone from user_info'")
	print stdout.readlines()
	print stderr
	ssh.close()


def sshclient_execmd(hostname, port, username, password, execmd):
	paramiko.util.log_to_file("paramiko.log")

	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	s.connect(hostname=hostname, port=port, username=username, password=password)
	stdin, stdout, stderr = s.exec_command(execmd)
	stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.

	print stdout.read()

	s.close()

def main():
	hostname = '10.***.***.**'
	port = 22
	username = 'root'
	password = '******'
	execmd = "free"

	sshclient_execmd(hostname, port, username, password, execmd)

def connection4():
	with SSHTunnelForwarder(
			ssh_address_or_host=('118.31.70.164', 9998),
			ssh_username='3602d0_root',
			ssh_password='Yfb111qqq',
			remote_bind_address=('rm-bp1qb3etnt3zb55oc.mysql.rds.aliyuncs.com', 3306)) as server:
		conn = MySQLdb.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
							   port=server.local_bind_port,
							   user='kld',
							   passwd='Kld123456',db='kld_lend_wealth')
		cursor = conn.cursor()
		cursor.execute("show tables")
		print(server.local_bind_address)
		print(len(cursor.fetchall()))

if __name__ == '__main__':
	connection4()
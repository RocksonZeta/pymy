# -*- coding:utf-8 -*- 
import pymy.mysqlx as mysqlx
mysqlx.dataSources.append(mysqlx.DataSource(host='localhost',
							user='root',
							password='yourpass',
							db="test",
							port=3000,
							))
@mysqlx.mysqli()
def get(con = None,con1=None):
	print(con.q("select * from users limit 10"))
	print(con.q1("select * from users limit 1"))
	print(con.qv("select count(*) from users limit 1"))

if '__main__' == __name__ :
	get()
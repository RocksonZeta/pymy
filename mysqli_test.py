# -*- coding:utf-8 -*- 
import mysqlx
mysqlx.dataSources.append(mysqlx.DataSource(host='localhost',
							user='root',
							password='yourpass',
							db="test",
							port=3000,
							))
@mysqlx.mysqli()
def get(con = None,con1=None):
	print(con.q("select * from users limit 1"))

if '__main__' == __name__ :
	get()
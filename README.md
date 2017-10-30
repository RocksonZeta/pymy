# pymy
python mysql utils

## installation
```
pip install git+https://github.com/RocksonZeta/pymy.git
```

## usage

```python
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
	#sql to list
	print(con.q("select * from users limit 10"))
	#sql to dict , fetch first row from resultset
	print(con.q1("select * from users limit 1"))
	#sql to value, fetch the first value of first row from resultset
	print(con.qv("select count(*) from users limit 1"))

if '__main__' == __name__ :
	get()
```

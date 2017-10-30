import pymysql
import time
dataSources = []
class DataSource:
	def __init__(self,host=None,port=3306,user='root',password=None,db=None,charset='utf8',cursorclass=pymysql.cursors.DictCursor , **kwargs):
		self.host= host
		self.port= port
		self.user= user
		self.password= password
		self.db= db
		self.charset= charset
		self.cursorclass= cursorclass
		self.pymysqlKwargs = kwargs
	def createConnection(self):
		"""create mysql connection """
		con = ConnectionEx(
						host=self.host,
						user=self.user,
						password=self.password,
						db=self.db,
						port=self.port,
						charset=self.charset,
						autocommit=True,
						cursorclass=self.cursorclass,**self.pymysqlKwargs
						)
		return con

class ConnectionEx(pymysql.connections.Connection):
	"""Mysql Connection"""
	def __init__(self , *args, **kwargs):
		pymysql.connections.Connection.__init__(self,*args, **kwargs)
		self.pageSize = 1000
	def q(self , *args):
		print("q",*args)
		with self.cursor() as cursor:
			cursor.execute(*args)
			return cursor.fetchall()
	def q1(self , *args):
		print("q1",*args)
		with self.cursor() as cursor:
			cursor.execute(*args)
			return cursor.fetchone()
	def qy(self , *args):
		print("qy",*args)	
		with self.cursor() as cursor:
			cursor.execute(*args)
			while True:
				rs = cursor.fetchmany(size=self.pageSize)
				if len(rs) <=0:
					break
				b = yield rs
				if bool == False or len(rs)<self.pageSize :
					break
	def qv(self , *args):
		print("qv",*args)
		with self.cursor() as cursor:
			cursor.execute(*args)
			r = cursor.fetchone()
			if r is None :
				return None
			for (_,v) in r.items():
				return v
	def truncate(self , *table):
		for t in table :
			self.q("truncate `"+t+"`")
		return self
	def maxId(self ,table , idFieldName = "id") :
		return self.qv("select ifnull(max("+idFieldName+"),0) from `"+ table+"`") 
	def count(self ,table , idFieldName = "id") :
		return self.qv("select count(*) from `"+ table+"`") 
	def disableFk(self):
		self.q('SET FOREIGN_KEY_CHECKS=0')
		return self
	def setAutoCommit(self , t):
		if t ==True :
			self.q('SET AUTOCOMMIT = 1')
		else :
			self.q('SET AUTOCOMMIT = 0')
		return self
	def enableFk(self):
		self.q('SET FOREIGN_KEY_CHECKS=1')
		return self
	def getCols(self , table):
		s = "select column_name,data_type  from information_schema.columns where table_schema='"+self.db+"' and table_name='"+table+"'"
		return self.q(s)
	def hasTable(self , table):
		return len(self.q("select * from information_schema.tables where table_schema='"+self.db+"' and table_name='"+table+"' limit 1")) >0
	


def mysqli(dsIndex=0,autoCommit = False,disableFk=True , name="con"):
	def decorator(func):
		def wrapper(*args , **kwargs):
			st = time.time()
			varnames = func.__code__.co_varnames
			con = None
			# print('varnames',varnames)
			if name in varnames :
				con = dataSources[dsIndex].createConnection()
				if disableFk :
					con.disableFk()
				con.setAutoCommit(autoCommit)
				kwargs[name] = con
			try:
				result = func(*args , **kwargs)
			finally:
				if con is not None :
					if disableFk :
						con.enableFk()
					if autoCommit == False :
						con.commit()
					con.close()
			et = time.time()
			print(func.__name__+" cost "+ str(et-st)+" sec")
			return result
		return wrapper
	return decorator

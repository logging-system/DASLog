import pymysql

#database config
db = pymysql.connect(host='your host name', user='your user name', password='your pass')
cursor = db.cursor()

#Create a database and table

sql = '''drop database LogDB'''
cursor.execute(sql)

sql = '''create database LogDB'''
cursor.execute(sql)

cursor.connection.commit()

sql = '''use LogDB'''
cursor.execute(sql)
#id int not null auto_increment,

sql = '''
create table ELogTable (
id int not null auto_increment,
lid VARCHAR(255),
time text,
EncData text,
log_address text,
log_block_number text,
primary key (id)
)
'''
cursor.execute(sql)

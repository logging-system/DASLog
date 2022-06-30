#sudo yum install mysql
#mysql -h database-1.cdqsjcaidv6a.eu-Anonymous.amazonaws.com -u C2C -p
#pass= scs13SCS!#
#pip install PyMySQL

import pymysql

#database config
db = pymysql.connect(host='loggingdb.cdqsjcaidv6a.Anonymous.rds.amazonaws.com', user='C2C', password='scs13SCS!#')
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
LogData text,
Tree_Index text,
log_address text,
log_block_number text,
primary key (id)
)
'''
cursor.execute(sql)

sql = '''
create table TreeTable (
iid int not null auto_increment,
rid VARCHAR(255),
tree_json LONGTEXT,
root_block_number text,
tree_hash_chain text,
root_tx_add text,
Tree_Index text,
primary key (iid)
)
'''

cursor.execute(sql)

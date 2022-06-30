import pymysql
import time
from subprocess import call

# Connect to the database
db = pymysql.connect(host='loggingdb.cdqsjcaidv6a.eu-Anonymous.amazonaws.com',
                            user='C2C',
                            password='scs13SCS!#',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.connection.commit()

sql = '''use LogDB'''
cursor.execute(sql)

j = 0
while True:

    if j == 0:
        sql4 = "SELECT `root_tx_add`, `Tree_Index` FROM `TreeTable` WHERE `root_block_number`=%s"
        cursor.execute(sql4, "waiting")
        result3 = cursor.fetchmany(1)
        print(result3)
        for item in result3:
            TxAdd = [item['root_tx_add']]
            TxIndx = [item['Tree_Index']]
        n = int(''.join(TxIndx))
        c = int(''.join(TxAdd))
    #print(type(c))
        print('index = ', n)
        print('address = ', c)
        with open('croot.txt', 'w') as pt4:
            pt4.write('%d' % c)
        rc = call("./TXcount.sh")
        print('fetch Information related to the Tx')
        with open('metadata.txt', 'r') as pt5:
            lines = pt5.read()
            pt5.close()
        print('metedata = ', lines)
        sql04 = '''
                UPDATE TreeTable SET root_block_number = %s WHERE `Tree_Index`=%s''' % ("'" + lines + "'", n)
        cursor.execute(sql04)
        db.commit()
    j = 1

    time.sleep(2.5)

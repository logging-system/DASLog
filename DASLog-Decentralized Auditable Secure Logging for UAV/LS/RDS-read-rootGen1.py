import pymysql
import base64
import json
import time
from cryptography.hazmat.primitives import hashes, hmac
from pymerkle import MerkleTree
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess


# Connect to the database
db = pymysql.connect(host='loggingdb.cdqsjcaidv6a.eu-west-2.rds.amazonaws.com',
                            user='C2C',
                            password='scs13SCS!#',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.connection.commit()

sql = '''use LogDB'''
cursor.execute(sql)


SizeOfInputsForTree = 5 #5000

with open('pointer.txt', 'w') as pt:
    pt.write('%d' % 0)
with open('pointer.txt', 'r') as pt:
    lines = pt.read()
with open('pointer2.txt', 'w') as pt2:
    pt2.write('%d' % 0)
with open('pointer2.txt', 'r') as pt2:
    lines2 = pt2.read()

pointer = int(lines) + 1
pointer2 = int(lines2) + 1

while True:
    sql1 = "SELECT `LogData` FROM `ELogTable` WHERE `id`>=%s"
    cursor.execute(sql1, pointer)
    result2 = cursor.fetchmany(SizeOfInputsForTree)
    #print(len(result2))

    tt_data = []
    for item in result2:
        t_data = [item['LogData']]
        tt_data.append(str(t_data))

    #with open('hashchain_data_file.txt', 'r') as pth:
    with open('scripts/hashchain_data_file.txt', 'r') as pth:
        linesh = pth.read()
        pth.close()
    if str(linesh) != '':
        tt_data.append(str(linesh))
    print(tt_data)
    open('scripts/hashchain_data_file.txt', 'w').close()
    #open('hashchain_data_file.txt', 'w').close()
    tree = MerkleTree()
    for record in tt_data:
        tree.encrypt(record)
    print(tree)
    #print(tree.size)
    print(tree.get_root_hash())
    Troot = tree.get_root_hash()

    if tree.size != 0:
        with open('pointer2.txt', 'w') as pt2:
            pt2.write('%d' % pointer2)
        with open('root.txt', 'w') as pt3:
            #pt3.write('%s' % Troot)
            pt3.write("0x"+str(Troot)[2:-1])
        print("send root to BC + pointer2")
        #rc = call("./WriteLog7.sh")
        subprocess.Popen(["node writeRoot2BC.js"], shell=True)

        RootTxcounter = pointer2
        tree.export('log_tree.json')
        print('send tree data to RDS')
        with open('log_tree.json', 'r') as f:
            tree_data = json.load(f)
        sql2 = '''
        insert into TreeTable(Tree_Index, tree_json, root_tx_add, root_block_number, tree_hash_chain) values('%s', '%s', '%s', '%s', '%s')''' % (pointer2, json.dumps(tree_data), RootTxcounter, "waiting", str(linesh))
        cursor.execute(sql2)
        db.commit()

        sql01 = '''
        UPDATE ELogTable SET LogData = null, Tree_Index = %s WHERE %s>`id`>=%s''' % (pointer2, pointer + len(result2), pointer)
        cursor.execute(sql01)
        db.commit()
        pointer2 = pointer2 + 1

        pointer = pointer + len(result2)
        print('p = ', pointer)
        with open('pointer.txt', 'w') as pt:
            pt.write('%d' % pointer)


    time.sleep(1)

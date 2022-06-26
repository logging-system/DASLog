import random
import base64
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
import subprocess
from subprocess import call
import pymysql

#added for the new merkle tree idea 9/6/2022
db = pymysql.connect(host='loggingdb.cdqsjcaidv6a.eu-west-2.rds.amazonaws.com', user='C2C', password='scs13SCS!#')
cursor = db.cursor()

cursor.connection.commit()

sql = '''use LogDB'''
cursor.execute(sql)
############################################

def Data_Analyser(u_data, L_N, Content_Type):
    if L_N == 1:
        open('scripts/hashchain_data_file.txt', 'w').close()
    with open('scripts/hashchain_data_file.txt') as f:
        old_hc = f.read()

    system_random = random.SystemRandom()

        # Read Log Data from Rest API
    data = u_data['message'].encode('utf-8')
        #data = b'this is the log of the system'
    print('\n'+"Log data: " + str(data))

        # Hashing
    digest = hashes.Hash(
                algorithm=hashes.SHA256(),
                backend=default_backend()
            )

        # CREATE HASH of LOG DATA
    digest.update(data)
    hash_string = digest.finalize()

    h_data = base64.urlsafe_b64encode(hash_string)# CONVERT/ENCODE IN BASE64

    print('\n'+"Hash of the data: 0x" + str(hash_string.hex()))
        # writing the hash of the log to the hash_data_file.json file
    with open("scripts/hash_data_file.txt", "w") as write_hfile:
        write_hfile.write("0x"+str(hash_string.hex()))
        write_hfile.close()
    if L_N == 1:
        with open("scripts/hashchain_data_file.txt", "w") as hcwrite_dfile:
            hcwrite_dfile.write("0x"+str(hash_string.hex()))
            hcwrite_dfile.close()
    else:
        data2 = old_hc[2:] + str(hash_string.hex())
        print('d2 = ', data2)
            # Hashing for hash-chain
        digest2 = hashes.Hash(
                    algorithm=hashes.SHA256(),
                    backend=default_backend()
                )

            # CREATE HASH of hash-chain
        digest2.update(data2.encode('utf-8'))
        new_hc = digest2.finalize()
        with open("scripts/hashchain_data_file.txt", "w") as hcwrite_dfile:
            hcwrite_dfile.write("0x"+str(new_hc.hex()))
            hcwrite_dfile.close()

    #rc = call("./WriteLog3.sh")

#added for the new merkle tree idea 9/6/2022
    with open('log_example.json', 'r') as f:
        lines = f.read()
    l_data = json.loads(lines)
    flight_ID = l_data['id'].encode('utf-8') + l_data['type'].encode('utf-8')

    # generate HMAC of the flight_ID: new idea
    hkey = b'60436092257359180159959298694639776512348204677813211341147137887844449615112'
    digest = hmac.HMAC(hkey, hashes.SHA256())
    digest.update(flight_ID)
    hmac_string = digest.finalize()
    ilid = str(hmac_string.hex())
    ##########################################

    # Read Log Data from File

    data = l_data['message'].encode('utf-8')

    # Encryption of log data
    sec = 50236095557359180159959298694639776544818204649813293341147137887852349615765
    salt = b'\t\xee2\xf7\xc4Jz\x1ez.\x1e6\x08K\n\xef'  # fixed

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        backend=default_backend(),
        iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(str(sec).encode()))
    f_key = Fernet(key)
    e_data = f_key.encrypt(data)
    iEncData = e_data.decode("utf-8")

    idata = str(data.decode("utf-8"))
    itime = l_data['timestamp']

    sql = '''
    insert into ELogTable(lid, time, EncData, LogData) values('%s', '%s', '%s', '%s')''' % (ilid, itime, iEncData, idata)
    cursor.execute(sql)
    db.commit()

    print('\n', "-----< Log information are stored in LogDB database >-----")

############################################

    msg = {'status': "true", 'ServerMessage': "LogDataStored"}
    return msg

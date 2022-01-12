import pymysql
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend

def Read_Data(u_data, u_flag):
    print(u_data)
    print(type(u_data))
    msg = {'status': "true", 'ServerMessage': "message", 'clientdata': "logData"}

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

        # Read a single record
    sql1 = "SELECT `EncData` FROM `ELogTable` WHERE `lid`=%s"
    sql2 = "SELECT `log_address` FROM `ELogTable` WHERE `lid`=%s"
    sql3 = "SELECT `log_block_number` FROM `ELogTable` WHERE `lid`=%s"

    flight_ID = u_data['id'].encode('utf-8') + u_data['type'].encode('utf-8')

    ''' Hash: old idea
        # generate hash of the flight_ID
    digest = hashes.Hash(
        algorithm=hashes.SHA256(),
        backend=default_backend()
    )

        # CREATE HASH of flight-id
    digest.update(flight_ID)
    hash_string = digest.finalize()
    ilid = str(hash_string.hex())
    '''

    # generate HMAC of the flight_ID: new ideai
    hkey = b'60436092257359180159959298694639776512348204677813211341147137887844449615112'
    digest = hmac.HMAC(hkey, hashes.SHA256())
    digest.update(flight_ID)
    hmac_string = digest.finalize()
    ilid = str(hmac_string.hex())
    ##########################################

    cursor.execute(sql1, ilid)
    result1 = cursor.fetchall()

    cursor.execute(sql2, ilid)
    result2 = cursor.fetchall()

    cursor.execute(sql3, ilid)
    result3 = cursor.fetchall()


        # Decryption
    sec = 50236095557359180159959298694639776544818204649813293341147137887852349615765
        #print("Secret key: "+ str(sec))
    salt = b'\t\xee2\xf7\xc4Jz\x1ez.\x1e6\x08K\n\xef'   #fixed
        #print("Salt: "+ str(salt))

    kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                backend=default_backend(),
                iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(str(sec).encode()))
    f_key = Fernet(key)
    i = 0
    dd_data = {}
    for item in result1:
        i = i+1
        d_data = {i: {'LogData_%s' % i: f_key.decrypt(item['EncData'].encode('utf-8'))}} # decrypted data
        dd_data = {**dd_data, **d_data[i]}

    i = 0
    dd_add = {}
    for item in result2:
        i = i+1
        d_add = {i: {'log_address_%s' % i: item['log_address']}}
        dd_add = {**dd_add, **d_add[i]}

    i = 0
    dd_bn = {}
    for item in result3:
        i = i+1
        d_bn = {i: {'log_block_number_%s' % i: item['log_block_number']}}
        dd_bn = {**dd_bn, **d_bn[i]}

    log_inf = {**dd_data, **dd_add, **dd_bn}

    with open("Log_file.txt", "w") as write_dfile:
        write_dfile.write(str(log_inf))
        write_dfile.close()
    akk = "LogData will be Sent to the User ...."
    msg.update(clientdata='%s'% str(log_inf))
    msg.update(ServerMessage='%s'% akk)

    return str(log_inf)

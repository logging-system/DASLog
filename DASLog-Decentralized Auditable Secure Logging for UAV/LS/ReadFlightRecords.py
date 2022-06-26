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


    flight_ID = u_data['id'].encode('utf-8') + u_data['type'].encode('utf-8')

    # generate HMAC of the flight_ID: new idea
    hkey = b'60436092257359180159959298694639776512348204677813211341147137887844449615112'
    digest = hmac.HMAC(hkey, hashes.SHA256())
    digest.update(flight_ID)
    hmac_string = digest.finalize()
    ilid = str(hmac_string.hex())
    ##########################################

    # Read Log Data from RDS


    sql5 = "SELECT * FROM `ELogTable` WHERE `lid`=%s"
    cursor.execute(sql5, ilid)
    result5 = cursor.fetchall()

    # Decryption
    sec = 50236095557359180159959298694639776544818204649813293341147137887852349615765
    # print("Secret key: "+ str(sec))
    salt = b'\t\xee2\xf7\xc4Jz\x1ez.\x1e6\x08K\n\xef'  # fixed
    # print("Salt: "+ str(salt))

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
    for item in result5:
        i = i + 1
        d_data = {i: {'LogData_%s' % i: f_key.decrypt(item['EncData'].encode('utf-8'))}}  # decrypted data
        dd_data = {**dd_data, **d_data[i]}
    i = 0
    dd_ind = {}
    dd_bn = {}
    dd_hc = {}
    dd_tj = {}
    for item in result5:
        i = i + 1
        d_ind = {i: {'Tree_Index_%s' % i: item['Tree_Index']}}
        sql6 = "SELECT `root_block_number` FROM `TreeTable` WHERE `Tree_Index`=%s"
        cursor.execute(sql6, item['Tree_Index'])
        result6 = cursor.fetchall()
        result6_string = ''.join(map(str, result6))
        d_bn = {i: {'log_root_block_number_%s' % i: eval(result6_string)['root_block_number']}}
        dd_ind = {**dd_ind, **d_ind[i]}
        dd_bn = {**dd_bn, **d_bn[i]}

        sql7 = "SELECT `tree_hash_chain` FROM `TreeTable` WHERE `Tree_Index`=%s"
        cursor.execute(sql7, item['Tree_Index'])
        result7 = cursor.fetchall()
        result7_string = ''.join(map(str, result7))
        d_hc = {i: {'log_hash_chain%s' % i: eval(result7_string)['tree_hash_chain']}}
        dd_hc = {**dd_hc, **d_hc[i]}

        sql8 = "SELECT `tree_json` FROM `TreeTable` WHERE `Tree_Index`=%s"
        cursor.execute(sql8, item['Tree_Index'])
        result8 = cursor.fetchall()
        result8_string = ''.join(map(str, result8))
        d_tj = {i: {'tree_json%s' % i: eval(result8_string)['tree_json']}}
        dd_tj = {**dd_tj, **d_tj[i]}
    log_inf = {**dd_data, **dd_bn, **dd_hc, **dd_tj}
    print(log_inf)

    with open("Log_file.txt", "w") as write_dfile:
        write_dfile.write(str(log_inf))
        write_dfile.close()


    akk = "LogData will be Sent to the User ...."
    msg.update(clientdata='%s'% str(log_inf))
    msg.update(ServerMessage='%s'% akk)

    return str(log_inf)

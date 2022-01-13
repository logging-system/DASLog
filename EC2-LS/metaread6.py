from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
import base64
import pymysql
import json

db = pymysql.connect(host='your host name', user='your user name', password='your pass')
cursor = db.cursor()

cursor.connection.commit()

sql = '''use LogDB'''
cursor.execute(sql)

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

# Encryption of data
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

#######Log address and Block number #######
with open('scripts/metadata.json') as f:
    lines = f.read()
res = json.loads(lines)
a = res[0]
b = a['blockNumber']
print('Block number:' + str(b))

c = a['address']
print('Box address:' + str(c))

ilog_address = c
ilog_block_number = b
###########################################

itime = l_data['timestamp']

sql = '''
insert into ELogTable(lid, time, EncData, log_address, log_block_number) values('%s', '%s', '%s', '%s', '%s')''' % (
ilid, itime, iEncData, ilog_address, ilog_block_number)
cursor.execute(sql)
db.commit()

print('\n', "-----< Log information are stored in LogDB database >-----")

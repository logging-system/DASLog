import ast
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import subprocess
import json

with open('Log_file.json') as f:
    lines1 = f.read()
lines = json.loads(lines1)
i = 1
log = ast.literal_eval(lines)['LogData_%s' % i]#.encode('utf-8')

while 'LogData_%s' % i in ast.literal_eval(lines):
    log = ast.literal_eval(lines)['LogData_%s' % i]
    ad_log = ast.literal_eval(lines)['log_address_%s' % i]
    bn_log = ast.literal_eval(lines)['log_block_number_%s' % i]
    
# Hashing
    digest = hashes.Hash(
                algorithm=hashes.SHA256(),
                backend=default_backend()
            )

# CREATE HASH
    digest.update(log)
    hash_string = digest.finalize()
    log_hash = hash_string.hex()
    with open("scripts/hash_log_file.txt", "w") as write_lfile:
        write_lfile.write('0x'+ str(hash_string.hex()))
        write_lfile.close()
    print("hash of the log: " + str(hash_string.hex()))

    with open("scripts/add_log_file.txt", "w") as write_lfile:
        write_lfile.write(str(ad_log))
        write_lfile.close()

    with open("scripts/bn_log_file.txt", "w") as write_lfile:
        write_lfile.write(str(bn_log))
        write_lfile.close()
    ###############Truffle###########
    subprocess.call('./truffle_r.sh')
    ###############Verify############
    with open('scripts/hash_log_file.txt') as f:
        lines0 = f.read()

    with open('scripts/value_in_add.txt') as f1:
        lines01 = '0x' + f1.read()

    with open('scripts/value_in_bn.txt') as f2:
        lines02 = '0x' + f2.read()

    if (lines0 == lines01) and (lines0 == lines02):
        print('===> Log number %s is verified ok ++++++' % i)
        print('Next Log ...')
    else:
        print('===> Log number %s is not verified ------' % i)
        print('Next Log ...')
    ################################

    i = i + 1
else:
    print('There is no other data to verify')
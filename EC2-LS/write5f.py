import random
import base64
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import subprocess
from subprocess import call

def Data_Analyser(u_data, u_flag, Content_Type):

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

    rc = call("./WriteLog3.sh")
    
    msg = {'status': "true", 'ServerMessage': "LogDataStored"}
    return msg

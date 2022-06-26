from pymerkle import MerkleTree
import random
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import hashlib
import ast
import json
from cryptography.hazmat.primitives import hashes, hmac
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from subprocess import call

def hashing_function(x):
    xin = '\x00'.encode('utf8') + x.encode('utf8')  # convert unicode string to a byte string
    m = hashlib.sha256()
    m.update(xin)
    return m.hexdigest()

with open('Log_file.json') as f:
    lines1 = f.read()
lines = json.loads(lines1)

i = 1
L_N = 1
f = 0
while 'LogData_%s' % i in ast.literal_eval(lines):
    log = ast.literal_eval(lines)['LogData_%s' % i]
    i = i+1
    system_random = random.SystemRandom()
        # Read Log Data from Rest API
    data = log
        # Hashing
    digest = hashes.Hash(
                algorithm=hashes.SHA256(),
                backend=default_backend()
            )

        # CREATE HASH of LOG DATA
    digest.update(data)
    hash_string = digest.finalize()
    h_data = base64.urlsafe_b64encode(hash_string)# CONVERT/ENCODE IN BASE64

    if L_N == 1:
        open('hashchain_data_file.txt', 'w').close()
    with open('hashchain_data_file.txt') as f:
        old_hc = f.read()

    h_data = base64.urlsafe_b64encode(hash_string)# CONVERT/ENCODE IN BASE64

        # writing the hash of the log to the hash_data_file.json file
    with open("hash_data_file.txt", "w") as write_hfile:
        write_hfile.write("0x"+str(hash_string.hex()))
        write_hfile.close()
    if L_N == 1:
        with open("hashchain_data_file.txt", "w") as hcwrite_dfile:
            hcwrite_dfile.write("0x"+str(hash_string.hex()))
            hcwrite_dfile.close()
    else:

        data2 = old_hc[2:] + str(hash_string.hex())
        # Hashing for hash-chain
        digest2 = hashes.Hash(
            algorithm=hashes.SHA256(),
            backend=default_backend()
        )

        # CREATE HASH of hash-chain
        digest2.update(data2.encode('utf-8'))
        new_hc = digest2.finalize()
        with open("hashchain_data_file.txt", "w") as hcwrite_dfile:
            hcwrite_dfile.write("0x" + str(new_hc.hex()))
            hcwrite_dfile.close()
    L_N = L_N + 1

R_hc_log = str(new_hc.hex())
print('Computed log_hash_chain = ', '0x'+R_hc_log)

hc_log = ast.literal_eval(lines)['log_hash_chain%s' % (i-1)]
print('received log_hash_chain = ', hc_log)

if R_hc_log == hc_log[2:]:
    print('Proof for received hashchain', "==>", 'True')
    f = 1
else:
    print('Proof for received hashchain', "==>", 'False')
    f = 0

i = 1
while 'log_hash_chain%s' % i in ast.literal_eval(lines):
    i = i+1

tp_log = ast.literal_eval(lines)['log_root_block_number_%s' % (i-1)]
with open('Thash.txt', 'w') as write_hfile:
    write_hfile.write(str(tp_log))
    write_hfile.close()

tj_log = ast.literal_eval(lines)['tree_json%s' % (i-1)]
with open('log_path1.json', 'w', encoding='utf-8') as jf:
    json.dump(json.loads(tj_log), jf, indent=4)
tree = MerkleTree()
loaded_tree = MerkleTree.fromJSONFile('log_path1.json')
# verify the root
state = loaded_tree.get_root_hash()
print("received root from LS = ", state)
rc = call("./Rproof.sh")
with open('bcroot.txt', 'r') as pt05:
    lines5 = pt05.read()
#RootFromBC = b'8c55aeb0b9a972ea07ceccbe2283dee16c1db5ee26cd3876416e44a892d4c2b4'
RootFromBC = hex(int(lines5))
print("received root from BC = ", RootFromBC)
proof = loaded_tree.generate_consistency_proof(challenge=RootFromBC)
# verify the hash_chain
hc_log = ast.literal_eval(lines)['log_hash_chain%s' % (i-1)]
#print('received log_hash_chain = ', hc_log)
H_hc_log = hashing_function(hc_log)
#print('Hash of the log_hash_chain = ', H_hc_log)
challenge0 = bytes(H_hc_log, 'utf-8')
proof0 = loaded_tree.generate_audit_proof(challenge0)

if proof.verify() and proof0.verify() and f == 1:
    print('Proof for received root from BC', "==>", proof.verify())
    print('proof of hash chain for %s logs' % (i - 1), "==>", proof0.verify())
else:
    print('Proof for received root from BC', "==>", proof.verify())
    print('proof of hash chain for %s logs' % (i - 1), "==>", proof0.verify())
    i = 1
    while 'LogData_%s' % i in ast.literal_eval(lines):
        log = ast.literal_eval(lines)['LogData_%s' % i]
        s_log = "['" + str(log)[2:-1] + "']"
        hc_log = ast.literal_eval(lines)['log_hash_chain%s' % i]
        bn_log = ast.literal_eval(lines)['log_root_block_number_%s' % i]
        tj_log = ast.literal_eval(lines)['tree_json%s' % i]
        H_hc_log = hashing_function(hc_log)
        H_log = hashing_function(s_log)
        with open('log_path1.json', 'w', encoding='utf-8') as jf:
            json.dump(json.loads(tj_log), jf, indent=4)
        tree = MerkleTree()
        loaded_tree = MerkleTree.fromJSONFile('log_path1.json')
        challenges = bytes(H_log, 'utf-8')
        # print('Hash of the LogData_%s' % i, '=', H_log)
        proofs = loaded_tree.generate_audit_proof(challenges)
        proofs.verify()
        print('LogData_%s' % i, "proof ==>", proofs.verify())
        i = i + 1

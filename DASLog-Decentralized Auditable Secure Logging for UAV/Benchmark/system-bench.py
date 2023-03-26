from pymerkle import MerkleTree
import time
import pandas as pd
from log_example_test import logs
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
import base64
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from log_sig_verify import verify_signature

# Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Sign log with private key
def sign_log(log_message):
    signature = private_key.sign(log_message,
                                 padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                                 hashes.SHA256())
    return signature

# hashing function
def hashing_function(x):
    m = hashlib.sha256()
    m.update(x.encode('utf8'))
    return m.hexdigest()


t = 100
nl = 100
tr = []
js = []
a = []
a1 = []
b = []
bhc = []
bsig = []
c = []
sec = 50236095557359180159959298694639776544818204649813293341147137887852349615765
salt = b'\t\xee2\xf7\xc4Jz\x1ez.\x1e6\x08K\n\xef'  # fixed

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    backend=default_backend(),
    iterations=100000)
key = base64.urlsafe_b64encode(kdf.derive(str(sec).encode()))

# Sign the log_data
log_data = str(logs())
sl = sign_log(log_data.encode("utf-8"))
#print('sl:', sl)

for j in range(1, t+1):

    n = j * nl # number of leaves
    Loglist = []
    for i in range(0, n):
        ldata = logs()
        Loglist.append(str(ldata))

    # Verify the signature
    tic_sig = time.process_time()
    verify_signature(public_key, log_data.encode("utf-8"), sl)
    toc_sig = time.process_time()

    tic = time.process_time()
    # hash_chain
    hc_log = ''
    for record in Loglist:
        hc_log = hashing_function(hc_log + str(hashing_function(record)))

    # Encryption of log data
        f_key = Fernet(key)
        e_data = f_key.encrypt(record.encode('utf-8'))
        iEncData = e_data.decode("utf-8")
    toc_DASLod = time.process_time()
    # Populate tree with records - Simple-DASLog
    #tic1 = time.process_time() #only MT
    tree = MerkleTree()
    for record in Loglist:
        tree.encrypt(record)
    print("number of leaves = ", len(Loglist))
    ts = tree.size
    tree.export('log_path.json')
    fs = os.stat('log_path.json').st_size
    js.append(str(fs * 0.001))  # KB
    toc = time.process_time()
    tr.append(str(ts*0.032))# KB
    #a1.append(str(toc - tic1)) #only MT
    a1.append(str(toc_DASLod - tic))  # DASLog
    a.append(str(toc - tic))  # Simple-DASLog
    c.append(str(n))
    # Prove and verify
    tic2 = time.process_time()
    hc_log_vr = ''
    for record in Loglist:
        hc_log_vr = hashing_function(hc_log_vr + str(hashing_function(record)))
    if hc_log_vr == hc_log:
        print('hashchain is verified')
    else:
        print('hashchain is not verified')

    toc02 = time.process_time()
    tic2_sig = time.process_time()
    loaded_tree = MerkleTree.fromJSONFile('log_path.json')

    state = loaded_tree.get_root_hash()
    # verify the root
    proof = loaded_tree.generate_consistency_proof(challenge=state)
    print(proof.verify())
    # verify the hash_chain
    challenge0 = bytes(hc_log, 'utf-8')
    proof0 = loaded_tree.generate_audit_proof(challenge0)
    toc2 = time.process_time()
    print(proof.verify())
    bhc.append(str(toc02 - tic2))
    b.append(str(toc2 - tic2))
    bsig.append(str((toc_sig - tic_sig) + (toc2 - tic2_sig)))

data = pd.DataFrame(
    {'C': c, 'A': a}
    )
with pd.ExcelWriter('tree_sheets_a.xlsx') as writer1:
    data.to_excel(writer1, sheet_name='df_1')

data = pd.DataFrame(
    {'C': c, 'A1': a1}
    )
with pd.ExcelWriter('tree_sheets_a1.xlsx') as writer1:
    data.to_excel(writer1, sheet_name='df_11')

data = pd.DataFrame(
    {'C': c, 'B': b}
    )
with pd.ExcelWriter('tree_sheets_b.xlsx') as writer1:
    data.to_excel(writer1, sheet_name='df_2')

data = pd.DataFrame(
    {'C': c, 'tr': tr}
    )
with pd.ExcelWriter('tree_sheets_tr.xlsx') as writer1:
    data.to_excel(writer1, sheet_name='df_3')

data = pd.DataFrame(
    {'C': c, 'js': js}
    )
with pd.ExcelWriter('tree_sheets_js.xlsx') as writer1:
    data.to_excel(writer1, sheet_name='df_4')

data = pd.DataFrame(
    {'C': c, 'Bhc': bhc}
    )
with pd.ExcelWriter('tree_sheets_bhc.xlsx') as writer1:
    data.to_excel(writer1, sheet_name='df_5')

data = pd.DataFrame(
    {'C': c, 'Bsig': bsig}
    )
with pd.ExcelWriter('tree_sheets_bsig.xlsx') as writer1:
    data.to_excel(writer1, sheet_name='df_6')

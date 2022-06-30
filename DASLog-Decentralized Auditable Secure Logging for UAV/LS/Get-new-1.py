import sys
from writeNew1 import Data_Analyser
from ReadFlightRecords import Read_Data
from flask import Flask, request
import json
import jwt
import base64
import socket
from ast import literal_eval
import os
#from subprocess import call

app = Flask(__name__)

#T_V = '0'
T_V = '1'
L_N = 0
Chapter_LN = 6
error = {'status': "Error", 'errorMessage': "RevokedUser|NotAuthorized|MisformedToken|etc"}
warning = {'status': "Warning", 'Message': "No data. Try again ..."}
def Token_val(R_W, Content_Type, accessid_token, data):
    try:
        global L_N
        with open("Log_file.txt", "w") as write_dfile:
            write_dfile.write(str(warning))
            write_dfile.close()
        if R_W == 'w': flag = "0"
        elif R_W == 'r': flag = "1"
        else:
            error.update(errorMessage='WrongRequest')
            return error
        if flag == "0":
            L_N += 1
            print("L_N=", L_N)
            if L_N == Chapter_LN:
                L_N = 0
            with open('log_example.json', 'w', encoding='utf-8') as ff:
                json.dump(data, ff,  indent=4)
            results = Data_Analyser(data, L_N, Content_Type)
        elif flag == "1":
        #replace KEYCLOAK_PUBLIC_KEY with yours
            KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgTP6yDoktGRyIhm/61KWXECS5GGkUb9q2NyEYYLYJCaFyaX/RsyDxiax+mokJ/+0N8H8iITsWxJ0+ggkB7frNZrfQSJZK6QjU6h2NLYuVZuxhYQgCL8rgC/Mg93BNgaYBEXtgeNZyaf4QRRdZAkG1jpevehIcNTJRLQK4IZGMevDHx8kkpO9QoUFv8aLYuAHiSoRR077s4lsDBlupDb/XuVwiXmQ389uyHsHSoBWF+XVzUmpgOuj3ISD/efE1iJvll1jhWWmIELdmbM28Ua9njDUDlJ2jt/E8DpGJ396CTNEmbZphGvV8+Ec716xH+b4cWxc5DeEG/2inBjqebIViQIDAQAB' + "\n-----END PUBLIC KEY-----"
            if T_V == '1':
                options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}
            else:
                options = {"verify_signature": False, "verify_aud": False, "verify_exp": False}
            decoded = jwt.decode(accessid_token, KEYCLOAK_PUBLIC_KEY, audience='account', algorithms=['RS256'], options = options)
            results = Read_Data(data, flag)
            print(decoded)
        #print(data)
        #print('sending data back to the client')
        return results
    except jwt.exceptions.ExpiredSignatureError:
        error.update(errorMessage='TokenHasExpired')
        return error
    except jwt.exceptions.DecodeError:
        error.update(errorMessage='InvalidToken')
        return error
    except jwt.exceptions.InvalidTokenError:
        error.update(errorMessage='InvalidToken')
        return error
    except ValueError:
        print("Oops!  That was no valid request.  Try again...")
@app.route('/Anonymous/write', methods = ['POST'])
def determine_escalation1():
    R_W = 'w'
    #global L_N
    jsondata = request.get_data()
    data = json.loads(jsondata)
    header = literal_eval(request.headers.get('Tokens'))
    if header['AuthToken'] == 's.JvKotVPg3HlQ1ZpchK6xerB':
        Content_Type = header['Content-Type']
        accessid_token = '*'
        return json.dumps(Token_val(R_W, Content_Type, accessid_token, data))
    else:
        error.update(errorMessage='UnAuthorizedUser')
        return json.dumps(error)

@app.route('/Anonymous/read', methods = ['POST'])
def determine_escalation2():
    R_W = 'r'
    jsondata = request.get_data()
    data = json.loads(jsondata)
    header = literal_eval(request.headers.get('Tokens'))
    if header['AuthToken'] == 's.JvKotVPg3HlQ1ZpchK6xerB':
        Content_Type = header['Content-Type']
        accessid_token = header['AccessToken']
        return json.dumps(Token_val(R_W, Content_Type, accessid_token, data))
    else:
        error.update(errorMessage='UnAuthorizedUser')
        return json.dumps(error)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

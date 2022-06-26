import sys, os, json
import socket

# Token from keycloak;user1

with open('KeycloakToken.txt') as f1:
        Acs_T = f1.read()

#Acs_T = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJMV3p5OERXQUVrZzJpQTNqckZUNllVZXZuU2VTVXBmSHJtNEhJbzBoMDRFIn0.eyJleHAiOjE2MzcxNDA0NDQsImlhdCI6MTYzNzEzOTg0NCwianRpIjoiMmJmODhmM2YtZDI0ZS00YzFhLTllOWEtZWQ0MGYwYWI5MzQ5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL0hBSS1TQ1MiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYjBjZTJhNDgtZTZlNC00YTg0LWIwZDgtMzE2NDZiNGQ3ZDk2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZmEtY29uc29sZSIsInNlc3Npb25fc3RhdGUiOiJkN2ZmZWM2Yi05ZDUxLTQyYjktODUwNC1iYjlhMzQ3MjdmZjgiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtaGFpLXNjcyIsIkhvc3BpdGFsLW4xIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJIQUktU0NTLUdyb3VwcyIsInNpZCI6ImQ3ZmZlYzZiLTlkNTEtNDJiOS04NTA0LWJiOWEzNDcyN2ZmOCIsImdyb3VwIjpbIi9Ib3NwaXRhbF9Hcm91cCJdfQ.bO0O4W70nG2ACpiqxqRJdrnyz7goLL9bV9mlWkbwYl__SDJKiZOQav4JbCRDur4hm6K6dq60tcRNqagaBZLungUfC7tdQ17d4wmdJthVW1qijlLGBKv3yboJAbLxA1dIQmIYKaPhoJ8hF60-sZbWNUVOZWkzKfJnqWBoIx6UCzxBMrVkrWpMc8N9-2qzdB5OmzCdbCpMCGPZ0i3oHnPuKx3X5uPw2rSOSehQUCcgc-9SfZNzqT7xoKm_gw8SoEaZBcNvS4dZ7ckv22dyI4xGUU8fcq2R7coyTYGB3y5ml9QJGek-Sp-av0cZApBoCYOkn10S5UZx3_V9Sw_dg3y-cA'

timestamp = '2021-11-15T09:39:00.346Z'
Content_Type = 'application/json'
Log_type = 'FLIGHT'#'Flight_ID'
Order_ID = 'ad30c4fe-885b-4b32-9de2-264eeb655d7f'#'ad30c4fe-885b-4b32-9de2-264eeb655d7f3'



data = {
        'type' : Log_type,
        'id': Order_ID
}


with open("data_hai.json", "w") as write_file:
    json.dump(data, write_file)


AuthToken = "s.JvKotVPg3HlQ1ZpchK6xerB"

X_token = "tokens: {'Content-Type': '%s', 'AccessToken': '%s', 'AuthToken': '%s'}"%(Content_Type, Acs_T, AuthToken)

os.system('curl -H "%s" --request POST --data @data_hai.json http://13.40.67.209:5000/KUL/hai/read>Log_file.json' % X_token)

print('Successfully received the Log_file.json')
'''
#socket module

port = 30310                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('I received', repr(data))
    with open('Log_file.txt', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = conn.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)
    f.close()
    #print('Successfully get the Log_file.txt')
    #conn.send(b'Thank you for connecting')
    conn.close()
    break
print('Successfully got the Log_file.txt')

'''

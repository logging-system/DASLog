import sys, os, json

# Token from keycloak;user1

with open('KeycloakToken.txt') as f1:
        Acs_T = f1.read()

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

os.system('curl -H "%s" --request POST --data @data_hai.json http://13.40.31.18:5000/KUL/hai/read>Log_file.json' % X_token)

print('Successfully received the Log_file.json')

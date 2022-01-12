import sys, os, json
from log_example import logs

ldata = logs()
for x in range(len(ldata)):
    if ldata[x]['timestamp']:
        timestamp = ldata[x]['timestamp']
        message = ldata[x]['message']
        Content_Type = 'application/json'
        Log_type = ldata[x]['type']
        Order_ID = ldata[x]['id']

        data = {
                'timestamp' : timestamp,
                'message': message,
                'type' : Log_type,
                'id': Order_ID
        }

        with open("data_hai.json", "w") as write_file:
            json.dump(data, write_file)

        AuthToken = "s.JvKotVPg3HlQ1ZpchK6xerB"

        X_token = "tokens: {'Content-Type': '%s', 'AuthToken': '%s'}"%(Content_Type, AuthToken)

        os.system('curl -H "%s" --request POST --data @data_hai.json http://13.40.31.18:5000/KUL/hai/write' % X_token)

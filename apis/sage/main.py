import json
import requests


class SageOne:

    def __init__(self):
        requests
        file = open('apis/sage/credentials/credentials.json')
        config = json.load(file)
        client_id = config['api']['client_id']
        callback_url = config['api']['callback_url']
        #print(config)

        r = requests.get(f"https://www.sageone.com/oauth2/auth?response_type=code&client_id={client_id}&redirect_uri={callback_url}&scope=full_access")
        #print(r.status_code)
        print(r.text)
import requests
from . import helper

def getToken(config):
    # Get the Token

    payload = {"client_id": {config['client_id']}, "client_secret": {config['client_secret']}, "code": {config['code']},
               "grant_type": "authorization_code"}
    response = requests.post(config['url_token'], data=payload)
    message = response.json()
    if response.ok:
        config['token'] = message['access_token']
        config['refresh_token'] = message['refresh_token']
        config['accountID'] = GetAccountID(config)
        helper.writeConfigToFile(config)
        time_left = message['expires_in'] / 60
        config['message'] = f'Success Token : {config["token"]}, expired in : {time_left} secondes'
        return config
    else:
        config['message'] = 'Access Code expired or communication error. Try re-click the link to get another access code'
        return config

def refreshToken(config):
    # Refresh the Token
    config = helper.readConfigFile(config)
    if config['message']:
        return 'Error : config file not found. Click on the click to get a access code'

    payload = {'refresh_token': config['refresh_token'], 'client_secret': config['client_secret'],
               'client_id': config['client_id'], 'grant_type': 'refresh_token'}
    r = requests.post(config['url_token'], data=payload)
    message = r.json()
    if r.ok:
        config['token'] = message['access_token']
        config['accountID'] = GetAccountID(config)
        helper.writeConfigToFile(config)
        time_left = message['expires_in'] / 60
        config['message'] = f'Success refresh Token : {config["token"]}, expired in : {time_left} secondes'
        return config
    else:
        config['message'] = 'Refresh token denied or communication error. Try re-click the link to get another access code'
        return config

def GetAccountID(config):
    url = 'https://api.lightspeedapp.com/API/Account.json'
    headers = {'Authorization':'Bearer ' + config['token']}
    r = requests.get(url, headers=headers)

    message = r.json()
    accountID = message['Account']['accountID']
    if r.ok:
        return accountID
    else:
        return 'no account ID'
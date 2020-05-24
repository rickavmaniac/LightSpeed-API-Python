from . import ls_auth, helper
import requests


def getAllItem(config):
    url = rf'https://api.lightspeedapp.com/API/Account/{config["accountID"]}/Item.json?load_relations=["ItemShops"]'
    headers = {'Authorization': 'Bearer ' + config['token']}
    r = requests.get(url, headers=headers)
    message = r.json()
    if r.ok:
        return message
    else:
       return 'Error retreiving item'
from django.shortcuts import render
import requests, json, os.path
from . import helper, ls_auth, ls_item, prestashop


# Create your views here.
def home(request):

    return render(request, 'home.html')


def lightpeed(request):
    # Get code from the return query from LightSpeed to our : localhost:8000/api?code=xyz
    code = request.GET.get('code')
    config = {}
    # Message only use for feedback to user
    config['message'] = ''
    config['code'] = code

    # Set the config value (you need to ask LightSpeed for those values (see documentation)
    config['client_id'] = '856f01aa3bb1ca8e8b7a8988e2e48ca6012d1c272d0661bbbc4c5f1fc1e46d34'
    config['client_secret'] = '5b32ce33ca48abf7de455f4cb35b7bee37115310dc72a73e096a1760f6efd4a0'

    # Url to click in order to get the access code from LightSpeed
    config[
        'url_access_code'] = rf'https://cloud.lightspeedapp.com/oauth/authorize.php?response_type=code&client_id={config["client_id"]}&scope=employee:all'
    # Url to Get the Token
    config['url_token'] = 'https://cloud.lightspeedapp.com/oauth/access_token.php'

    # Once you click on the link the page will submit to itself and reload with the ?code parameter fulfill
    # If first attempt and if a code is provide in the query : call GetToken method
    # if no code provide and not first attempt : Read token from config.json file
    if code:
        config = ls_auth.getToken(config)

    else:
        config = ls_auth.refreshToken()



    return render(request, 'ls_api.html', {'config': config })


def item(request):
    config = ls_auth.refreshToken()
    item = ls_item.getAllItem(config)
    item = item['Item']
    return render(request, 'item.html', {'item': item })


def order_to_process(request):
    data = prestashop.get_order_data()
    return render(request, 'ordertoprocess.html', {'data': data })


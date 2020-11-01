#!/usr/bin/env python
import requests
#from getpass import getpass, getuser

my_vmanage = {
    'vmanage_ip': '10.10.20.90',
    'vmanage_port': '8443',
    'vmanage_user': 'admin',
    'vmanage_pass': 'C1sco12345'
    }

#VMANAGE_PASS = getpass('Enter vmanage password: ')

def login(vmanage_ip, vmanage_port, vmanage_user, vmanage_pass):
    base_url = 'https://{}:{}'.format(vmanage_ip, vmanage_port)
    login_endpoint = '/j_security_check'

    payload = { 'j_username': vmanage_user, 'j_password': vmanage_pass }

    headers = { 'Content-Type': 'x-www-form-urlencoded' }

    url = base_url + login_endpoint

    response = requests.request('POST', url, data=payload, verify=False)

    if '<html>' in response.text:
        print('Login to VMANAGE Failed')
        sys.exit(1)
    else:
        jsessionid = response.headers['Set-Cookie'].split(';')[0]

    return jsessionid

def token(vmanage_ip, vmanage_port, jsessionid):
    base_url = 'https://{}:{}'.format(vmanage_ip, vmanage_port)
    token_endpoint = '/dataservice/client/token'

    url = base_url + token_endpoint

    headers = { 'Cookie': jsessionid }

    response = requests.request('GET', url, headers=headers, verify=False)

    if response.status_code == 200:
        token = response.text
        return token
    else:
        print('No token has been acquired')
        return None

def craft_header(jsessionid, token):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': jsessionid,
        'X-XSRF-TOKEN': token
        }

    return headers

def get_data(vmanage_ip, vmanage_port, endpoint, headers):
    base_url = 'https://{}:{}'.format(vmanage_ip, vmanage_port)
    get_endpoint = endpoint

    url = base_url + get_endpoint

    response = requests.request('GET', url, headers=headers, verify=False)

    return response

def post_data(vmanage_ip, vmanage_port, endpoint, headers, payload={}):
    base_url = 'https://{}:{}'.format(vmanage_ip, vmanage_port)
    post_endpoint = endpoint

    url = base_url + post_endpoint

    data = json.dumps(payload)
    
    response = requests.request('POST', url, headers=headers, data=data, verify=False)

    return response

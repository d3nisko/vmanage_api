#!/usr/bin/env python
import requests
from getpass import getpass, getuser

VMANAGE_IP = '10.10.20.90'
VMANAGE_PORT = '8443'
VMANAGE_USER = 'admin'
VMANAGE_PASS = 'C1sco12345'
#VMANAGE_PASS = getpass('Enter vmanage password: ')


def login(vmanage_ip, vmanage_port, user, password):
    '''Crafting the url'''    
    BASE_URL_STR = 'https://{}:{}/'.format(vmanage_ip, vmanage_port)
    LOGIN_ACTION = '/j_security_check'
    '''Payload to login'''
    LOGIN_DATA = { 'j_usernae': user, 'j_password': password }
    
    LOGIN_URL = BASE_URL_STR + LOGIN_ACTION
    
    sess = requests.session()
    
    login_response = sess.post(url=LOGIN_URL, data=LOGIN_DATA, verify=False)
    
    if login_response.status_code != 200:
        print('Login Failed')
        sys.exit(1)
    else:
        return(login_response)

def get_request(vmanage_ip, vmanage_port, mount_point):
    '''Crafting the url'''
    url = 'https://{}:{}/dataservice/{}'.format(vmanage_ip, vmanage_port, mount_point)

    '''Accessing the data'''
    requests.request('GET', url, verify=False)
    data = response.content
    return data

def post_request(vmanage_ip, vmanage_port, resource, payload, \
                 headers={'Content-Type': 'application/json'}):
    '''Crafting the url'''
    url = 'https://{}:{}/dataservice/{}'.format(vmanage_ip, vmanage_port, resource)
    
    payload = json.dumps(payload)

    response = requests.request('POST', url, data=payload, headers=headers, verify=False)
    data = response.json()

    return data


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

my_test = login(VMANAGE_IP,VMANAGE_PORT,VMANAGE_USER,VMANAGE_PASS)
print(type(my_test))

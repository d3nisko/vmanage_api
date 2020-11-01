#!/usr/bin/env python
import requests
from getpass import getuser, getpass

class rest_api_lib:
    def __init__(self, vmanage_ip, vmanage_port, username, password):
        self.vmanage_ip = vmanage_ip
        self.vmanage_port = vmanage_port
        self.session = {}
        self.login(self.vmanage_ip, self.vmanage_port, username, password)

    def login(self, vmanage_ip, vmanage_port, username, password):
        '''Crafting the url'''
        BASE_URL_STR = 'https://{}:{}/'.format(vmanage_ip, vmanage_port)
        LOGIN_ACTION = '/j_security_check'
        '''Payload to login'''
        LOGIN_DATA = { 'j_usernae': username, 'j_password': password }
 
        LOGIN_URL = BASE_URL_STR + LOGIN_ACTION

        sess = requests.session()

        login_response = sess.post(url=LOGIN_URL, data=LOGIN_DATA, verify=False)

        if login_response.status_code != 200:
            print('Login Failed')
            sys.exit(1)

        self.session[vmanage_ip] = sess

    def get_request(self, resource):
        '''Crafting the url'''
        url = 'https://{}:{}/dataservice/{}'.format(self.vmanage_ip, self.vmanage_port, resource)

        '''Accessing the data'''
        response = requests.request('GET', url, verify=False)
        data = response.content
        return data

    def post_request(self, resource, payload, \
                     headers={'Content-Type': 'application/json'}):
        '''Crafting the url'''
        url = 'https://{}:{}/dataservice/{}'.format(self.vmanage_ip, self.vmanage_port, resource)
    
        payload = json.dumps(payload)
    
        response = self.session('POST', url, data=payload, headers=headers, verify=False)
        data = response.json()
    
        return data

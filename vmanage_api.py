#!/usr/bin/env python
import requests
import json
import os
import sys

#class VmanageAuth:

#    def __init__(self, vmanage_ip, vmanage_port, username, password):

def Authenticate(vmanage_ip, vmanage_port, vmanage_user, vmanage_pass):
    base_url = 'https://{}:{}/'.format(vmanage_ip, vmanage_port)
    auth_endpoint = 'j_security_check'

    url = base_url + auth_endpoint

    payload = { 'j_username': vmanage_user, 'j_password': vmanage_pass }

    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    
    response = requests.request('POST', url, headers=headers, data=payload, verify=False)

    if response.status_code == 200:
        try:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            if logger is not None:
                logger.error("No valid JSESSION ID returned\n")
            exit()

def GetToken(vmanage_ip, vmanage_port, jsessionid):
    base_url = 'https://{}:{}/'.format(vmanage_ip, vmanage_port)
    token_endpoint = 'dataservice/client/token'

    headers = {'Cookie': jsessionid}
    
    url = base_url + token_endpoint

    response = requests.request('GET', url, headers=headers, verify=False)

    if response.status_code == 200:
        return(response.text)
    else:
        return None

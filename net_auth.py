import requests
import time
import os
import json

url = 'http://172.16.253.3:801/eportal/'
s = requests.Session()

def get_ip():
    ip = json.loads(os.popen('ip -j address').read())[-1]['addr_info'][0]['local']
    return ip

def get_cookies():
    headers = {
        'Host': '172.16.253.3:801',
        'Referer': 'http://172.16.253.3/'
    }
    params = {
        'c': 'Portal',
        'a': 'lang',
        'program_name': 'andxxml',
        'web_type': 'ip',
        'page_index': '1',
        'i18n_lang': 'zh-CN'
    }
    s.get(url, headers=headers, params=params)

def login(ip):
    get_cookies()
    params = {
        'c': 'Portal',
        'a': 'login',
        'callback': 'dr{}'.format(int(time.time() * 1000)),
        'login_method': '1',
        'user_account': 'YXXXXXXXX', # replace it with your user id
        'user_password': 'password', # replace it with your password
        'wlan_user_ip': '{}'.format(ip),
        'wlan_user_mac': '000000000000',
        'wlan_ac_ip': '',
        'wlan_ac_name': '',
        'jsVersion': '3.0'
    }
    s.get(url, params=params)
    res = s.get(url, params=params)
    print(res.text.encode('ISO-8859-1').decode('utf-8'))

def main():
    ip = get_ip()
    login(ip)

if __name__ == '__main__':
    main()

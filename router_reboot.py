import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

ROUTER_WEB_INTERFACE_ADDR = 'http://192.168.1.1/'
PAGE_ADDR = 'userRpm/SysRebootRpm.htm'

ADMIN_USER_NAME = 'admin'
ADMIN_PASSWORD = ''

print('User name:', ADMIN_USER_NAME)
ADMIN_PASSWORD = getpass('Password (hint: as user): ')

form_data = {'Reboot': 'Reboot'}

r = requests.get(ROUTER_WEB_INTERFACE_ADDR + PAGE_ADDR,
                    auth=HTTPBasicAuth(ADMIN_USER_NAME, ADMIN_PASSWORD), 
                    params=form_data)

print('Status code: %s' % r.status_code)
print('Content: \n%s\s' % r.content)

if r.status_code == 200:
    print('OK')
else:
    print('FAILED')



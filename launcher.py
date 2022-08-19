from getpass import getpass
import requests, sys

WEB_HEADERS = {
    'User-Agent': 'Sunrise Games Python Launcher',
    'From': 'me@rocketprogrammer.me'
}

params = {
    'username': input('Username: '),
    'password': getpass('Password: ')
}

try:
    request = requests.post('https://sunrise.games/api/login/alt/', data = params, headers = WEB_HEADERS)
    data = request.json()
except:
    print('Failed to authenticate with web.')
    sys.exit(0)

if  data['success']:
    # Successful login.
    os.environ['LOGIN_TOKEN'] = data['token']

    from toontown.launcher import QuickStartLauncher
else:
    # Login failed.
    print(data['message'])
    sys.exit(1)
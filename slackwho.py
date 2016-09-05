#!/usr/bin/env python3
import json
import sys
import os
from collections import defaultdict

from slackclient import SlackClient

CONFIG_FILENAME = os.path.join(
    os.path.dirname(__file__),
    'accounts.json')

try:
    channels = json.loads(open(CONFIG_FILENAME).read())
except FileNotFoundError:
    print('Error reading config from {}'.format(CONFIG_FILENAME))
    print('File not found')
    sys.exit(1)
except json.decoder.JSONDecodeError as jse:
    print('Error reading config from {}'.format(CONFIG_FILENAME))
    print(jse)
    sys.exit(1)

online = defaultdict(list)
for account_name, token in channels.items():
    sc = SlackClient(token)
    users = sc.api_call("users.list")
    for user in users['members']:
        userid = user['id']
        username = user['name']
        presence = sc.api_call('users.getPresence', user=userid)
        if presence['presence'] == 'away':
            continue
        online[username].append(account_name)

print(':: slackwho ::')
for username, channel_list in sorted(online.items()):
    print('{} ({})'.format(
        username,
        ', '.join(sorted(channel_list))
    ))

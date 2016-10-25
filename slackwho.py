#!/usr/bin/env python3
import json
import sys
import os
from datetime import datetime
from collections import defaultdict
from requests.exceptions import ConnectionError

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

now = datetime.now()
online = defaultdict(list)
for account_name, token in channels.items():
    sc = SlackClient(token)
    try:
        users = sc.api_call("users.list")
    except ConnectionError:
        print('<api connection error>')
        sys.exit(1)
    for user in users['members']:
        userid = user['id']
        username = user['name']
        presence = sc.api_call('users.getPresence', user=userid)
        if presence['presence'] == 'away':
            continue
        dnd = sc.api_call('dnd.info', user=userid)
        next_dnd_end = datetime.fromtimestamp(dnd['next_dnd_end_ts'])
        next_dnd_start = datetime.fromtimestamp(dnd['next_dnd_start_ts'])
        if next_dnd_start < now < next_dnd_end:
            username += '-dnd'
        online[username].append(account_name)

print(':: slackwho ::')
if '--html' in sys.argv:
    print('<br />')

max_username_length = len(max(online.keys(), key=len))
for username, channel_list in sorted(online.items()):
    # bold username, tab, channel list
    if '--html' in sys.argv:
        format_string = ('<span class="username">{}</span>'
                         '<span class="channels">{}</span><br />')
    else:
        format_string = '\033[1m{}\033[0m\t{}'

    print(format_string.format(
        username.ljust(max_username_length, ' '),
        ', '.join(sorted(channel_list))
    ))

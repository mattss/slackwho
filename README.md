# slackwho
At-a-glance multi-account presence checker for Slack
Designed for use with [GeekTool](https://www.tynsoe.org/v2/geektool/) or similar.

## Why?

I have multiple slack accounts for various groups and organisations, and wanted
a way to quickly see an overview of who was online.

This script uses the [Slack API](https://api.slack.com/) to generate a text contacts list of all users
who are online across the slack accounts that you configure.

You can use something like [GeekTool](https://www.tynsoe.org/v2/geektool/)
or [Übersicht](http://tracesof.net/uebersicht/)
to stick the output of it on your desktop.

## Requirements

Python 3

## Config

 * Create an accounts.json, mapping account names to api tokens:


        {"slack account 1": "token-for-account-1",
         "slack account 2": "token-for-account-2"
         }

    *(Generate personal API tokens at https://api.slack.com/web#authentication)*

 * Create a virtualenv and activate

 * Install requirements

     pip install -r requirements.txt

## Run

    python3 slackwho.py

## Output

All online users, followed by the account(s) they are active on.

    :: slackwho ::
    user1   accountlist
    user2   accountlist
    user3   accountlist

## HTML Output

    python3 slackwho.py --html

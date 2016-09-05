# slackwho
At-a-glance multi-account presence checker for Slack

Designed for use with geektool or similar.

## Config

 * Create an accounts.json, mapping account names to api tokens:


    {"slack account 1": "token-for-account-1",
     "slack account 2": "token-for-account-2"
     }

    **(Generate personal API tokens at https://api.slack.com/web#authentication)**

 * Create a virtualenv and activate

 * Install requirements

     pip install -r requirements.txt

## Run

    python slackwho.py

## Output

All online users, followed by the account(s) they are active on.

    user1 (accountlist)
    user2 (accountlist)
    user3 (accountlist)

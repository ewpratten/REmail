# REmail
An email relay written in python

## Usage
To make use of these relays, sendn email to one of the relay addresses below.

To specify who to send the email to, add this line to the start of the email.
```
Format:
:username:domain:tld:

Example:
:bob:gmail:com:
```

## List of emails
This is the list of REmail accounts out on the web. Feel free to add your own.

| Email | Maintainer | Verified? | Refresh Time |
| ----- | ---------- | --------- | ------------ |
| remail.dev@gmail.com | @ewpratten | YES | Manual |

## TODO
 - automatic email checking using ping-pong
 - hop count specified in config
  - picks from random list of verified emails untill hop counter hits 0, then send to RCPT
 - Anon mode
 - Credit mode

## Setting up the gmail account
bla bla This bit isnt finished.

`pip install -r requirements.txt`

Save the json file to `~/.remail/credentials.json`



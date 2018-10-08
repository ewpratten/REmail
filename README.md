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

<!--start_emails-->
| Email | Maintainer | Verified? | Refresh Time | Logs Kept? |
| ----- | ---------- | --------- | ------------ | ---------- |
| remail.dev@gmail.com | @ewpratten | YES | 30s | Yes (STDout and gmail) |
<!--end_emails-->
## TODO
 - hop count specified in config
  - picks from random list of verified emails untill hop counter hits 0, then send to RCPT
 - Anon mode
 - Credit mode

## Setting up your own relay
To set up your own relay, you will need a gmail account. You can make one on the Google website.

Next, on a linux device, make a file at `~/.remail/login.conf`. Its contents should look like:
```
USERNAME@gmail.com
PASSWORD

```

Next, clone this repo, then `cd` into it.

Now, make sure you have python3 and pip installed, then install the required libraries:
```sh
python3 -m pip install -r requirements.txt
```

Next, run:
```sh
python3 src/
```
This will parse through your unread emails and respond / forward them.
It is recommended to add the above command to your crontab to automatically refresh your email buffer.

To update the program, run:
```sh
git pull
```

Thats it! Feel free to add your new email address to the list above!

## Running the relay on DigitalOcean (The cheaty way)
Spin up a droplet and make sure you have the tools installed, then follow the instructions above.

Next, install `screen`

Then, run:
```sh
screen
python3 src/ &
Ctrl-a + d
```
# Messenger Bot Tester

I wanted a tool to write basic test cases for my messenger bot so I made this.


### Disclaimer

This is really barebones and hacked together tool at the moment but I am hoping to improve it. Feel free to post issues or feature requests.


# Setup

Install Python 2.7

```
git clone https://github.com/Fraser-Greenlee/bot_tester.git
cd bot_tester
pip install -r requirements.txt
```

Reset your sending url to `http://0.0.0.0:8888` for testing.

Set `send_to` in `testbot/__init__.py` to your local bot url.

To run the server and the test cases.

`python __init__.py`

# Basic Usage

Define user with a random new id.

`user = testbot.User()`

Send a postback from the user.

`user.postback(postback_key)`

Test the user received a message.

`user.did_receive("What is your favourite colour?")`

if True:

`[True, msg.replace('\n',' \ ')]`

if False:

`[False, expected, got/error]`

> Best to append these results to a list and use `testbot.results(myResults)`

Send a text message from the user.

`user.send("blue")`

Send an attachment from the user.

`user.send({'type':"image",'payload':{'url':'http://blahblah.com'}})`

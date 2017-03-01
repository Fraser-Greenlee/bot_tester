# Messenger Bot Tester

I wanted a tool to write basic test cases for my messenger bot so I made this.


### Disclaimer

This is really barebones at the moment but I am hoping to imporve it. Feel free to post issues or feature requests.


# Setup

Install Python 2.7

```
git clone https://github.com/Fraser-Greenlee/bot_tester.git
cd bot_tester
pip install requirements.txt
```

Reset your sending url to http://0.0.0.0:8888 for testing.

Run server and test cases.

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

Test the user received a message. And append to results list.

`results.append( user.did_receive("Got it!") )`

Show the test results.

`testbot.results(results)`

# slack-hermes

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mdcg/slack-hermes/blob/master/LICENSE)

:email: *A message notifier for Slack written in Python*

## Overview

Hermes is a bot to help you send notifications to Slack channels. Basically it was created to help with service monitoring, where we basically needed to check if the service had stopped or if it had been completed.

Below is an example of how it is used:

```python
import os
from hermes import Hermes

hermes_bot = Hermes(
    slack_token=os.environ['SLACK_API_TOKEN'],
    channel="#hermes-notifier",
)
hermes_bot.send_message(
    message="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    message_type="info",
)
```

If you check the channel `#hermes-notifier`, you will see the following message:

<<IMG>>

## First steps


Before installing Hermes, I strongly recommend that you read the following tutorial: [Create a Slack app](https://github.com/slackapi/python-slackclient/blob/master/tutorial/01-creating-the-slack-app.md).

You will need to perform some steps described in this tutorial for the full functioning of Hermes. 

Once you have set it up: 

- Go to Slack;
- create a channel (or if you prefer, use an existing one);
- click on the gear icon located in the upper corner;
- click on the option "add an app";
- select the app you created;
- VOILÀ!

To check if everything went well, below is a small snippet:

```python
from hermes import Hermes

hermes_bot = Hermes(
    slack_token="INSERT_YOUR_SLACK_TOKEN_HERE",
    channel="#INSERT_YOUR_CHANNEL_HERE",
)
hermes_bot.send_message(
    message="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    message_type="info",
)
```

*PS: Be careful not to forget the **#** in front of the channel name, otherwise it will not work!*

## Installation

Use the package manager pip to install Hermes.

```
pip install -e "git+git@github.com:mdcg/slack-hermes.git@master#egg=slack-hermes"
```

## Messages types

There are currently only two types of messages that Hermes supports: Error messages and informational messages.

```python
import os
from hermes import Hermes

hermes_bot = Hermes(
    slack_token=os.environ['SLACK_API_TOKEN'],
    channel="#hermes-notifier",
)

# Info message
hermes_bot.send_message(
    message="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    message_type="info",
)

# Error message
hermes_bot.send_message(
    message="Nam imperdiet leo ac nisl tristique, eu bibendum quam consectetur.",
    message_type="error",
)
```

In the slack you will receive something like this:

<<IMG>>

*PS: If you pass a type that does not exist, exception `HermesInvalidMessageType` will be raised.*

## Contributing

Feel free to do whatever you want with this project. :-)

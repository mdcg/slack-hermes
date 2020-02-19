import getpass
import os
import platform
from datetime import datetime

import slack

from .exceptions import HermesInvalidMessageType


class Hermes(object):
    def __init__(self, slack_token, channel):
        """Hermes builder, who will establish some important connections with Slack
        
        Parameters
        ----------
        slack_token : str
            Hermes app authentication token.
        channel : str
            name of the channel on which Hermes will send its notifications.
            Example: #random, #general, etc.
        """
        self.client = slack.WebClient(token=slack_token)
        self.channel = channel

    def _get_os_informations(self):
        """Get generic information from the Operating System to facilitate
        the identification of the machine that is running a certain service.

        Returns
        -------
        dict
            Dictionary containing some generic information like ...
        """
        return {
            "user": getpass.getuser(),
            "dist": " ".join(dist_info for dist_info in platform.dist()),
            "system": platform.system(),
            "machine": platform.machine(),
            "current_datetime": datetime.now().strftime("%d %B, %Y - %H:%M:%S"),
        }

    def choose_message_type(self, message_type):
        """Return a template based on the chosen message type.

        Parameters
        ----------
        message_type : str
            Choose the type of message to be sent, which can be INFO or ERROR.

        Returns
        -------
        str
            Template with the chosen message type
        """
        options = {
            "INFO": "**INFO:** ",
            "ERROR": "**ERROR:** ",
        }
        try:
            selected_option = options[message_type.upper()]
        except KeyError:
            raise HermesInvalidMessageType

        return selected_option

    def format_message(self, message, message_type):
        """Concatenates the data obtained from the platform and the operating
        system to send to the Slack.

        Parameters
        ----------
        message : str
            Message informed by the service using Hermes, which may be
            end-of-processing messages, errors, etc.
        message_type : str, optional
            Choose the type of message to be sent, which can be INFO or ERROR.

        Returns
        -------
        str
            Returns a friendly message, containing data that makes it easy to
            find which machine the service is running on, ready to be sent to Slack
        """
        os_informations = self._get_os_informations()
        base_message = (
            f"[{os_informations['current_datetime']}] - "
            f"{os_informations['dist']}, "
            f"{os_informations['system']}, "
            f"{os_informations['machine']}, "
            f"User: {os_informations['user']} => "
        )
        message_type = self.choose_message_type(message_type)
        return base_message + message_type + message

    def send_message(self, message, message_type="INFO"):
        """Send the message to Slack.

        Parameters
        ----------
        message : str
            Message informed by the service using Hermes, which may be
            end-of-processing messages, errors, etc.
        message_type : str, optional
            Choose the type of message to be sent, which can be INFO or ERROR,
            by default 'INFO'
        """
        formated_message = self.format_message(message, message_type)
        self.client.chat_postMessage(channel=self.channel, text=formated_message)

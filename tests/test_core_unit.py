import os
import unittest

from .lib.core import Hermes


class HermesUnitTests(unittest.TestCase):
    def setUp(self):
        self.hermes = Hermes(os.environ["SLACK_API_TOKEN"], "#random")

    def test_format_message(self):
        pass

    def test_send_message(self):
        # Mock in client.chat_postMessage
        pass


if __name__ == "__main__":
    unittest.main()

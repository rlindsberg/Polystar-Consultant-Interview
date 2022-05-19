import socket
import unittest

from models.message import Message
from modles.server import Server
from controller import Controller


class TestController(unittest.TestCase):
    def test_send(self):
        """
        Given one line of text,
        When send() to an echoing server,
        Then received message matches the original message.
        """
        text = 'A very very simple text.'
        msg = Message(text)
        echo_server = Server()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((echo_server.server_ip, echo_server.server_port))

            client = Controller(s)

            ok, res = client.send(msg)

            self.assertTrue(ok)
            self.assertIsNotNone(res)

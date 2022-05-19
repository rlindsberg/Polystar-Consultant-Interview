import socket
import unittest
from threading import Thread

from models.message import Message
from models.echo_server import EchoBaseServer
from controller import Controller


class TestController(unittest.TestCase):
    def test_send_header(self):
        """
        Given one line of text,
        When send_header() to an echoing server,
        Then received message matches the original message.
        """
        echo_server = EchoBaseServer('127.0.0.1', 50001)
        t1 = Thread(target=echo_server.start)
        t1.start()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect(('127.0.0.1', 50001))

            client = Controller(s)
            text = 'A message of 21 bytes'
            msg = Message(text, client)

            ok, res = client.send_header(msg._header)

            self.assertTrue(ok)
            self.assertIsNotNone(res)
            self.assertEqual(res, b'21')
            print(res)

    def test_send_text(self):
        """
        Given one line of text,
        When send_text() to an echoing server,
        Then decoded received message matches the original text.
        """
        echo_server = EchoBaseServer('127.0.0.1', 50001)
        t1 = Thread(target=echo_server.start)
        t1.start()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 50001))

            client = Controller(s)
            text = 'A very very simple text.'

            ok, res = client.send_text(text)

            self.assertTrue(ok)
            self.assertIsNotNone(res)
            self.assertEqual(res, text)
            print(res)

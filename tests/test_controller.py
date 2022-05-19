import socket
import unittest
from threading import Thread

from models.message import Message
from models.echo_server import EchoServer
from controller import Controller


class TestController(unittest.TestCase):
    def test_send_header(self):
        """
        Given one line of text,
        When send_header() to an echoing server,
        Then received message matches the original message.
        """
        def send_to_server():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.0001)
                s.connect(('127.0.0.1', 50001))

                client = Controller(s)
                text = 'A message of 21 bytes'
                msg = Message(text, client)

                ok, res = client.send_header(msg._header)

                self.assertTrue(ok)
                self.assertIsNotNone(res)
                self.assertEqual(res, b'21')
                print(res)

        echo_server = EchoServer('127.0.0.1', 50001)
        t1 = Thread(target=echo_server.start)
        t1.start()

        t2 = Thread(target=send_to_server)
        t2.start()
        t2.join()

import json
import socket
from typing import Tuple, Dict, Union

from models.message import Message


class Controller:
    """
    The logic of the counter program. Both client and server uses controller to send and receive messages.
    """
    def __init__(self, socket_connection):
        self.conn = socket_connection

    def receive_from_socket(self, length: int) -> Tuple[bool, Union[bytes, None]]:
        try:
            res = self.conn.recv(length)
            return True, res

        except ConnectionResetError:
            return False, None

    def _send_header(self, header_to_send: bytes) -> Tuple[bool, Union[bytes, None]]:
        try:
            self.conn.sendall(header_to_send)

            # res = self.conn.recv(1024)
            ok, res = self.receive_from_socket(1024)
            if not ok:
                return False, None

        except socket.timeout as e:
            print(e)
            res = None

        # Verify result
        if res == header_to_send:
            return True, res
        else:
            return False, res

    def _send_payload(self, msg: Message) -> Tuple[bool, Union[bytes, None]]:
        self.conn.sendall(msg.payload)

        # res = self.conn.recv(msg.length).decode(msg.encoding)
        ok, res = self.receive_from_socket(msg.length)
        if not ok:
            return False, None

        text = res.decode(msg.encoding)
        if text == msg.text:
            return True, res
        else:
            return False, res

    def send_text(self, text: str) -> Tuple[bool, Union[str, None]]:
        msg = Message(text, self)

        ok, res = self._send_header(msg.header)

        if not ok:
            print('Send header failed.')
            return False, None
        else:
            # continue
            ok, res = self._send_payload(msg)
            res = res.decode('utf-8')

            if not ok:
                print('Send message payload failed.')
                return False, None
            else:
                return ok, res

    def send_dict(self, json_dict: Dict) -> Tuple[bool, Union[bytes, None]]:
        data = json.dumps(json_dict)
        msg = Message(data, self)

        ok, res = self._send_header(msg.header)

        if not ok:
            print('Send header failed.')
            return False, None
        else:
            # continue
            self._send_payload(msg)

            return ok, res

    def receive_dict(self) -> Tuple[bool, Union[Dict, None]]:
        # header = self.conn.recv(1024)
        ok, header = self.receive_from_socket(1024)
        if not ok:
            return False, None

        self.conn.sendall(header)
        payload_size = int(header.decode('utf-8'))

        # client stores json dump, sends res - sendall()
        # data = self.conn.recv(payload_size)
        ok, data = self.receive_from_socket(payload_size)
        if not ok:
            return False, None

        self.conn.sendall(data)

        json_dict = json.loads(data)

        return True, json_dict

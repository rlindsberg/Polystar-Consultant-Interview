import json
import socket
from typing import Tuple, Dict, Union

from models.message import Message

from models.codes import Codes


class Controller:
    """
    The logic of the counter program. Both client and server uses controller to send and receive messages.
    """
    def __init__(self, socket_connection):
        self.conn = socket_connection

    def receive_from_socket(self, length: int) -> Tuple[Codes, Union[bytes, None]]:
        try:
            res = self.conn.recv(length)
            return Codes.OK, res

        except ConnectionResetError:
            return Codes.ABORTED, None

    def _send_header(self, header_to_send: bytes) -> Tuple[Codes, Union[bytes, None]]:
        try:
            self.conn.sendall(header_to_send)

            # res = self.conn.recv(1024)
            ok, res = self.receive_from_socket(1024)
            if ok != Codes.OK:
                return Codes.ABORTED, None

        except socket.timeout as e:
            print(e)
            res = None

        # Verify result
        if res == header_to_send:
            return Codes.OK, res
        else:
            return Codes.DATA_LOSS, res

    def _send_payload(self, msg: Message) -> Tuple[Codes, Union[bytes, None]]:
        self.conn.sendall(msg.payload)

        # res = self.conn.recv(msg.length).decode(msg.encoding)
        ok, res = self.receive_from_socket(msg.length)
        if ok != Codes.OK:
            return Codes.ABORTED, None

        text = res.decode(msg.encoding)
        if text == msg.text:
            return Codes.OK, res
        else:
            return Codes.DATA_LOSS, res

    def send_text(self, text: str) -> Tuple[Codes, Union[str, None]]:
        msg = Message(text, self)

        ok, res = self._send_header(msg.header)

        if ok != Codes.OK:
            print('Send header failed.')
            return ok, None
        else:
            # continue
            ok, res = self._send_payload(msg)
            res = res.decode('utf-8')

            if ok != Codes.OK:
                print('Send message payload failed.')
                return ok, None
            else:
                return ok, res

    def send_dict(self, json_dict: Dict) -> Tuple[Codes, Union[bytes, None]]:
        data = json.dumps(json_dict)
        msg = Message(data, self)

        ok, res = self._send_header(msg.header)

        if ok != Codes.OK:
            print('Send header failed.')
            return ok, None
        else:
            # continue
            self._send_payload(msg)

            return ok, res

    def receive_dict(self) -> Tuple[Codes, Union[Dict, None]]:
        # header = self.conn.recv(1024)
        ok, header = self.receive_from_socket(1024)
        if ok != Codes.OK:
            return ok, None

        self.conn.sendall(header)
        payload_size = int(header.decode('utf-8'))

        # client stores json dump, sends res - sendall()
        # data = self.conn.recv(payload_size)
        ok, data = self.receive_from_socket(payload_size)
        if ok != Codes.OK:
            return ok, None

        self.conn.sendall(data)

        json_dict = json.loads(data)

        return ok, json_dict

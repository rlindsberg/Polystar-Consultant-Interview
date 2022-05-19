import json
import socket

from models.message import Message


class Controller:
    def __init__(self, socket_connection):
        self.conn = socket_connection

    def send_header(self, header_to_send):
        try:
            self.conn.sendall(header_to_send)
            res = self.conn.recv(1024)
        except socket.timeout as e:
            print(e)
            res = None

        # Verify result
        if res == header_to_send:
            return True, res
        else:
            return False, res

    def _send_payload(self, msg):
        self.conn.sendall(msg.payload)
        res = self.conn.recv(msg.length).decode(msg.encoding)

        if res == msg.text:
            return True, res
        else:
            return False, res

    def send_text(self, text: str):
        msg = Message(text, self)

        ok, res = self.send_header(msg.header)

        if not ok:
            raise Exception('Send header failed.')
        else:
            # continue
            ok, res = self._send_payload(msg)

            if not ok:
                raise Exception('Send message payload failed.')
            else:
                return ok, res

    def send_dict(self, json_dict):
        data = json.dumps(json_dict)
        msg = Message(data, self)

        ok, res = self.send_header(msg.header)

        if not ok:
            raise Exception('Send header failed.')
        else:
            # continue
            self._send_payload(msg)

    def receive_dict(self):
        header = self.conn.recv(1024)
        self.conn.sendall(header)
        payload_size = int(header.decode('utf-8'))

        # 5. client stores json dump, sends res - sendall()
        data = self.conn.recv(payload_size)
        self.conn.sendall(data)

        json_dict = json.loads(data)

        return json_dict

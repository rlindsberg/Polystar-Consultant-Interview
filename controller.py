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

    def send_payload(self, msg):
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
            ok, res = self.send_payload(msg)

            if not ok:
                raise Exception('Send message payload failed.')
            else:
                return ok, res

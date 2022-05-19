import socket


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

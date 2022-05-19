# echo-server.py
# This code is inspired by https://realpython.com/python-sockets/#echo-server
import socket

from models.base_server import BaseServer


class EchoBaseServer(BaseServer):
    def __init__(self, server_ip, server_port):
        super().__init__(server_ip, server_port)

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.server_ip, self.server_port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

import argparse
import json
import socket
from collections import Counter
import re
from typing import Dict

from controller import Controller


def count_word_frequencies(text: str) -> Dict:
    words = re.findall(r'\w+', text.lower())
    fre_list = Counter(words)
    return dict(fre_list)


def start(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind(('127.0.0.1', port))
        s.listen()

        while True:
            client_socket, addr = s.accept()
            controller = Controller(client_socket)

            # 2. server stores header, sends res - sendall()
            data_received = controller.conn.recv(1024)
            # while socket is open
            while data_received != b'':
                print(f'2. I got {data_received}')
                payload_size = int(data_received.decode('utf-8'))

                controller.conn.sendall(data_received)

                # 5. server stores payload, sends res - sendall()
                payload = controller.conn.recv(payload_size)
                controller.conn.sendall(payload)

                # server computes word frequency
                text = payload.decode('utf-8')
                f_dict = count_word_frequencies(text)

                controller.send_dict(f_dict)

                # the very end, wait for next packet
                data_received = controller.conn.recv(1024)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=50000, type=int, help='The socket port')
    args = parser.parse_args()

    start(args.port)

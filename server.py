import json
import socket
from collections import Counter
import re
from typing import Dict


def count_word_frequencies(text: str) -> Dict:
    words = re.findall(r'\w+', text.lower())
    fre_list = Counter(words)
    return dict(fre_list)


def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((socket.gethostname(), 50001))
        s.listen()

        while True:
            client_socket, addr = s.accept()

            # 2. server stores header, sends res - sendall()
            data_received = client_socket.recv(1024)
            # while socket is open
            while data_received != b'':
                print(f'2. I got {data_received}')
                payload_size = int(data_received.decode('utf-8'))

                client_socket.sendall(data_received)

                # 5. server stores payload, sends res - sendall()
                payload = client_socket.recv(payload_size)
                print(f'5. I got {payload}')
                client_socket.sendall(payload)

                # server computes word frequency
                text = payload.decode('utf-8')
                f_list = count_word_frequencies(text)
                print(f_list)

                data = json.dumps(f_list)
                print('Sending json dump!')
                # 1. server sends header - send_header()
                payload_size = len(data)
                header = str(payload_size).encode('utf-8')
                client_socket.sendall(header)

                # 3. server checks res == header
                res = client_socket.recv(1024)
                print(f'3. I got {res}')

                if res != header:
                    raise Exception('Sent message was corrupted.')
                else:
                    # continues
                    # 4. server sends json dump - send_json_dump()
                    payload = bytes(data, encoding="utf-8")
                    client_socket.sendall(payload)

                    # 6. server checks res == json dump
                    res = client_socket.recv(payload_size)

                    if res != payload:
                        raise Exception('Sent message was corrupted.')

                    # the very end, wait for next packet
                    data_received = client_socket.recv(1024)


if __name__ == '__main__':
    start()

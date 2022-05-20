import socket
from collections import Counter
from threading import Thread, Lock
from os import listdir
from os.path import isfile, join
from tqdm import tqdm

from controller import Controller

server_ip_list = ['poly.karlemstrand.com', 'star.karlemstrand.com']
server_port_list = [50000, 50001]
thread_list = []
final_word_frequency_dict = {}


def count(host: str, port: int, file_path: str, lock: Lock):
    global final_word_frequency_dict

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        client = Controller(s)

        with open(file_path) as f:
            print(file_path)
            for line in tqdm(f):
                client.send_text(line)

                res = client.receive_dict()

                with lock:
                    for key, val in res.items():
                        try:
                            final_word_frequency_dict[key] += val
                        except KeyError:
                            final_word_frequency_dict[key] = val
        print('Done!')


def main():
    data_path = '/Users/karlemstrand/Documents/git/HiQ/data/novels'
    files = [join(data_path, f) for f in listdir(data_path) if isfile(join(data_path, f))]

    for i, file_path in enumerate(files):
        host = server_ip_list[i]
        port = server_port_list[i]
        lock = Lock()

        t = Thread(target=count, args=(host, port, file_path, lock))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    top_k_counter = Counter(final_word_frequency_dict).most_common(5)
    top_k_dict = dict(top_k_counter)
    print(f'The 5 most common words in the two texts are: {top_k_dict}')

    return top_k_dict


if __name__ == '__main__':
    main()

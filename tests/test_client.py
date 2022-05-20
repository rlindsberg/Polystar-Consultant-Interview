import time
import unittest
from threading import Thread
import client

import server


class TestController(unittest.TestCase):
    def test_final_results(self):
        # setup two servers
        threads = []
        server_port_list = [50000, 50001]
        n_threads = 2

        for i in range(n_threads):
            t = Thread(target=server.start, args=(server_port_list[i],))
            threads.append(t)

        for t in threads:
            t.start()

        time.sleep(1)

        # count
        word_frequency_dict_top_5 = client.main()

        # test
        ground_truth = {'the': 12483, 'and': 9018, 'i': 7692, 'to': 6919, 'of': 6517}
        self.assertEqual(word_frequency_dict_top_5, ground_truth)

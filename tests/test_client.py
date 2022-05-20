import time
import unittest
from threading import Thread
import client

import server


class TestController(unittest.TestCase):
    def test_final_results(self):
        # count
        word_frequency_dict_top_5 = client.main()

        # test
        ground_truth = {'the': 12483, 'and': 9018, 'i': 7692, 'to': 6919, 'of': 6517}
        self.assertEqual(word_frequency_dict_top_5, ground_truth)

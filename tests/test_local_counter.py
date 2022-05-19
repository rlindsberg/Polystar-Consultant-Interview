import unittest
from pathlib import Path

from models.base_counter import BaseCounter


class TestLocalCounter(unittest.TestCase):
    def test_count_single_line(self):
        """
        Given one line of text,
        When count_word_frequencies(),
        Then output matches the manually counted result.
        """
        text = 'A very very simple text.'
        base_counter = BaseCounter(text)

        word_frequency_dict = base_counter.count_word_frequencies()

        self.assertEqual(word_frequency_dict['a'], 1)
        self.assertEqual(word_frequency_dict['very'], 2)
        self.assertEqual(word_frequency_dict['simple'], 1)
        self.assertEqual(word_frequency_dict['text'], 1)

        # edge cases
        with self.assertRaises(KeyError):
            self.assertEqual(word_frequency_dict['A'], 1)

        with self.assertRaises(KeyError):
            self.assertEqual(word_frequency_dict[' '], 4)

        with self.assertRaises(KeyError):
            self.assertEqual(word_frequency_dict['.'], 1)

    def test_count_multiple_files(self):
        """
        Given path to the directory containing multiple input files,
        When count_word_frequencies_in_directory(),
        Then output matches the manually counted result.
        """
        # setup
        data_path = '/Users/karlemstrand/Documents/git/HiQ/data/test_count_multiple_files'
        Path(data_path).mkdir(parents=True, exist_ok=True)

        base_counter = BaseCounter(data_path=data_path)

        with open(f'{data_path}/single_line.txt', "w") as text_file:
            text_file.write('A very very simple text.')

        with open(f'{data_path}/poly_line.txt', "w") as text_file:
            text_file.write('A very very simple text\n')
            text_file.write('A very very simple text\r\n')
            text_file.write('A very very simple text.')

        word_frequency_dict = base_counter.count_word_frequencies_in_directory()

        # testing
        self.assertEqual(word_frequency_dict['a'], 4)
        self.assertEqual(word_frequency_dict['very'], 8)
        self.assertEqual(word_frequency_dict['simple'], 4)
        self.assertEqual(word_frequency_dict['text'], 4)

        # edge cases
        with self.assertRaises(KeyError):
            self.assertEqual(word_frequency_dict['texta'], 2)

    def test_count_word_in_two_novels(self):
        data_path = '/Users/karlemstrand/Documents/git/HiQ/data/novels'
        base_counter = BaseCounter(data_path=data_path)

        word_frequency_dict = base_counter.count_word_frequencies_in_directory(top_k=5)

        # print(word_frequency_dict)
        # [('the', 12483), ('and', 9018), ('i', 7692), ('to', 6919), ('of', 6517)]

        self.assertIsNotNone(word_frequency_dict)
        self.assertEqual(len(word_frequency_dict), 5)

        for _, val in word_frequency_dict.items():
            # top 5 words has at least one occurrence each
            self.assertGreater(val, 0)

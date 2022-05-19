import unittest

from models.base_counter import BaseCounter


class TestLocalCounter(unittest.TestCase):
    def test_count_single_line(self):
        """
        Given one line of text,
        When count_word_frequencies(),
        Then output matches the manually counted result.
        """
        text = 'A very very simple text.'
        base_counter = BaseCounter()

        word_frequency_dict = base_counter.count_word_frequencies(text)

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

import re
from typing import Dict
from os import listdir
from os.path import isfile, join

from collections import Counter

from server import count_word_frequencies


class BaseCounter:
    def __init__(self, text: str = None, data_path: str = None):
        self.text = text
        self.data_path = data_path

    def count_word_frequencies_in_directory(self, top_k: int = None) -> Dict:
        mypath = self.data_path

        files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

        final_word_frequency_dict = {}
        for file_path in files:
            with open(file_path) as f:
                for line in f:
                    words = re.findall(r'\w+', line.lower())
                    fre_list = Counter(words)
                    data = dict(fre_list)

                    for key, val in data.items():
                        try:
                            final_word_frequency_dict[key] += val
                        except KeyError:
                            final_word_frequency_dict[key] = val

        if top_k is not None:
            top_k_counter = Counter(final_word_frequency_dict).most_common(top_k)
            final_word_frequency_dict = dict(top_k_counter)

        return final_word_frequency_dict

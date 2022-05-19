from collections import Counter
import re
from typing import Dict


class BaseCounter:
    def __init__(self, text: str):
        self.text = text

    def count_word_frequencies(self) -> Dict:
        words = re.findall(r'\w+', self.text.lower())
        fre_counter = Counter(words)
        return dict(fre_counter)

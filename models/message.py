

class Message:
    def __init__(self, text, controller):
        self.encoding = 'utf-8'
        self._text = text
        self._payload = self._text.encode(self.encoding)
        self._length = len(self._payload)
        self._header = str(self._length).encode(self.encoding)
        self.controller = controller
        self.ok = False

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

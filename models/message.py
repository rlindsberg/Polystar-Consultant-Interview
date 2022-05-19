

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

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: str):
        self._header = header

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, payload: str):
        self._payload = payload

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length: str):
        self._length = length

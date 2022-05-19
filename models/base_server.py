from abc import ABC, abstractmethod


class BaseServer(ABC):
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    @abstractmethod
    def start(self):
        pass

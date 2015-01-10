import logging
import socket


MAX_UDP_PAYLOAD = 568


def _chunkit(it, chunklength, prefix):
    max_length = chunklength - len(prefix)
    for i in range(0, len(it), max_length):
        yield prefix + it[i:i + max_length]


def _chunker(it, chunklength, prefix=b""):
    assert chunklength > len(prefix)
    if len(it) <= chunklength:
        yield it
    else:
        yield from _chunkit(it, chunklength, prefix)


class UdpHandler(logging.Handler):
    level = logging.DEBUG

    def __init__(self, ip, port):
        logging.Handler.__init__(self)
        self.address = ip, port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def emit(self, record):
        for idx, msg in enumerate(self._get_chunks(record)):
            self.socket.sendto(msg, self.address)

    def _get_chunks(self, record):
        return _chunker(self._tobytes(record), MAX_UDP_PAYLOAD, b"*** ")

    def _tobytes(self, r):
        return bytes(self.format(r), "utf-8")

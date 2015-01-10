import argparse
from udphandler import UdpHandler
import logging
import sys


def getargs():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main(args):
    logging.basicConfig()
    l = logging.getLogger()
    l.addHandler(UdpHandler("10.11.14.133", 5004))
    l.setLevel(logging.DEBUG)
    l.debug("blub")
    l.debug("blu\u2929b")
    try:
        raise ValueError()
    except Exception as e:
        l.exception(e)
    l.debug("b" * 600)
    return 0


if __name__ == '__main__':
    sys.exit(main(getargs()))

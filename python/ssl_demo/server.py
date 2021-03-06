#!/usr/bin/env python

import sys, traceback, json
from gevent.server import StreamServer

def echo(socket, address):
    try:
        while True:
            _buffer = socket.recv(4096)
            if not _buffer:
                return
            socket.sendall(_buffer)
    except Exception, e:
        print traceback.format_exc()
    finally:
        socket.close()


if __name__ == '__main__':
    keyfile = "/home/cloudzhou/script/python/ssl_demo/suibian.com.key"
    certfile = "/home/cloudzhou/script/python/ssl_demo/suibian.com.crt"
    server_ssl = StreamServer(('0.0.0.0', 9443), echo, keyfile=keyfile, certfile=certfile)
    server_ssl.serve_forever()


#!/usr/bin/env python3
# coding=utf-8
# title          : myhttpd.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/24 12:37
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s', self.path)


def main():
    try:
        server = HTTPServer(('', 8080), MyHandler)
        print('Welcom to the machine...')
        print('Prescc ^C to quit.')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down.')
        server.socket.close()


if __name__ == '__main__':
    main()

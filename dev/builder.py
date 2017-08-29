#!/usr/bin/env python3
"""
bot submission interface
* take bot source code (zip pack)
* extract, compile and run
"""

# TODO:
#     exit on request (get/head)
#     extract compile and run submited bot (with subprocess?, sync/async?, bg/fg?)

from http.server import BaseHTTPRequestHandler, HTTPServer
from re import findall
from os import path

class Handler(BaseHTTPRequestHandler):
    """
    handle http request from network
    * upload bot (zip) to run
    * get bot result
    """

    # def do_HEAD(self):
    #     print("do_HEAD")
    #     self.send_response(500)
    #     self.end_headers()

    # def do_GET(self):
    #     print("do_GET")
    #     self.send_response(500)
    #     self.end_headers()

    def do_POST(self):
        print("do_POST")

        headers = self.headers
        for h in headers:
            print(h, headers[h])

        r, info = self.deal_post_data()
        if r:
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(400)
            self.end_headers()

    # https://gist.github.com/touilleMan/eb02ea40b93e52604938
    def deal_post_data(self):
        # TODO: refactor this method

        content_type = self.headers['content-type']
        if not content_type:
            return (False, "Content-Type header doesn't contain boundary")

        boundary = content_type.split("=")[1].encode()
        remainbytes = int(self.headers['content-length'])

        line = self.rfile.readline()
        remainbytes -= len(line)

        if not boundary in line:
            return (False, "Content NOT begin with boundary")

        line = self.rfile.readline()
        remainbytes -= len(line)

        fn = findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode())
        if not fn:
            return (False, "Can't find out file name...")
        fn = path.join('.', fn[0])
        print(fn)

        line = self.rfile.readline()
        remainbytes -= len(line)
        line = self.rfile.readline()
        remainbytes -= len(line)

        try:
            out = open(fn, 'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?")

        preline = self.rfile.readline()
        remainbytes -= len(preline)

        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)

            if boundary in line:
                preline = preline[0:-1]
                if preline.endswith(b'\r'):
                    preline = preline[0:-1]
                out.write(preline)
                out.close()
                return (True, "File '%s' upload success!" % fn)
            else:
                out.write(preline)
                preline = line

        return (False, "Unexpect Ends of data.")

PORT = 8000

def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print("serving at port", PORT)
    httpd.serve_forever()

run()

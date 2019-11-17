"""
A fan server script, checking for a 'PUT' method and json-serialized data.
Working with 'raspberry_admin.py' script for an initiation of enable/disable a fan.
"""

import ast
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# from .raspberry_admin import fan_command


class LiteServerHandler(BaseHTTPRequestHandler):
    """
    Class for handling income HTTP-connections with POST methods only.
    """

    def _set_headers(self):
        self.send_response(200, message=None)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        """
        Main method of this LiteServerHandler.
        Start reaction on data.
        """
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self.react_to_command(post_data)

    @staticmethod
    def react_to_command(data):
        """
        Setting voltage to Raspberry Pi 3 pin, enabling and shutting down a fan.

        Param 'data' -- json serialized file.
        """

        decoded_data = json.loads(data)
        decoded_data = dict(ast.literal_eval(decoded_data))
        srv_cmd = decoded_data['command']

        if (srv_cmd != 'enable') and (srv_cmd != 'shutdown'):
            raise Exception('Incorrect command type')

        voltage = 'LOW'
        if srv_cmd == 'enable':
            voltage = 'HIGH'
        print('EXCELLENT', voltage)
        # fan_command(voltage)


def run_server(server_class=HTTPServer, handler_class=LiteServerHandler, port=5500):
    """
    Starting forever running server.
    Daemon-look, waiting for 'POST' request from main Django-Server.
    """
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == "__main__":
    run_server()

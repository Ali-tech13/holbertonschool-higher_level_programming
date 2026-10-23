
#!/usr/bin/python3
"""Simple RESTful API using Python's http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    """Handle incoming HTTP requests."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            json_conv = json.dumps(data)
            self.wfile.write(json_conv.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            infos = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            json_conv = json.dumps(infos)
            self.wfile.write(json_conv.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    server.serve_forever()

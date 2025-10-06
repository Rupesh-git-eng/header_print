from http.server import BaseHTTPRequestHandler, HTTPServer

class HeaderLoggingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log client IP, path, and headers
        print(f"\n[REQUEST] {self.client_address[0]}:{self.client_address[1]} {self.command} {self.path}")
        print("Headers:")
        for header, value in self.headers.items():
            print(f"  {header}: {value}")

        # Respond with a simple message
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello! Headers logged to server console.\n")

    def log_message(self, format, *args):
        # Suppress default HTTP server logging
        return

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8080
    print(f"Starting server on {HOST}:{PORT} ...")
    with HTTPServer((HOST, PORT), HeaderLoggingHandler) as server:
        server.serve_forever()

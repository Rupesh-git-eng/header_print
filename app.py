from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Configure logging
logging.basicConfig(
    filename="headers.log",        # log file name
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

class HeaderLoggingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]

        logging.info("===================================")
        logging.info(f"REQUEST: {client_ip}:{self.client_address[1]} {self.command} {self.path}")

        # Log headers
        logging.info("Headers:")
        for header, value in self.headers.items():
            logging.info(f"{header}: {value}")

        logging.info("===================================\n")

        # Response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello! Headers logged to file.\n")

    def log_message(self, format, *args):
        return  # suppress default logging


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8080

    print(f"Starting server on {HOST}:{PORT} ...")
    with HTTPServer((HOST, PORT), HeaderLoggingHandler) as server:
        server.serve_forever()

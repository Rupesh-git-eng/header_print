from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("headers.log", "a") as f:
            f.write(f"\n--- Request from {self.client_address[0]} ---\n")
            for k, v in self.headers.items():
                f.write(f"{k}: {v}\n")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Logged\n")

    def log_message(self, format, *args):
        return  # silence default logs

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

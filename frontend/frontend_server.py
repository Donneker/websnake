from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

# standard server extended to serve CORS headers
class CORSRequestHandler (SimpleHTTPRequestHandler):
    # add CORS headers here
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        return super(CORSRequestHandler, self).end_headers()

if __name__ == '__main__':
    host = sys.argv[1] if len(sys.argv) > 2 else '0.0.0.0'
    port = int(sys.argv[len(sys.argv)-1]) if len(sys.argv) > 1 else 8000
    print("Listening on {}:{}".format(host, port))
    httpd = HTTPServer((host, port), CORSRequestHandler)
    httpd.serve_forever()

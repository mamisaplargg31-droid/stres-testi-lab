from http.server import BaseHTTPRequestHandler, HTTPServer
import math
import os

class TestServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # İşlemciyi test etmek için matematik döngüsü
        hesaplama = 0
        for i in range(100000):
            hesaplama += math.sqrt(i)

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("anneni sikiom orospu cocu\n".encode("utf-8"))

if __name__ == '__main__':
    # Render'ın atadığı portu otomatik yakalar (Bulamazsa 10000 kullanır)
    port = int(os.environ.get("PORT", 10000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, TestServer)
    print(f"Sunucu aktif, port {port} dinleniyor...")
    httpd.serve_forever()

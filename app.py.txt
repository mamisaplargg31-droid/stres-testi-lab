from http.server import BaseHTTPRequestHandler, HTTPServer
import math

class TestServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # ─── SUNUCUYU BİLEREK YORAN STRATEJİK KOD ───
        # Her ziyaretçide arka planda ağır bir matematik hesabı döndürüyoruz.
        # Bu sayede stres testi aracı yüklendiğinde sunucu işlemcisi (CPU) 
        # hızla tıkanacak ve gerçek bir siber saldırı etkisi yaratacaktır.
        Agir_hesaplama = 0
        for i in range(500000):
            agir_hesaplama += math.sqrt(i)

        # ─── ZİYARETÇİYE GÖNDERİLEN YANIT ───
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("🤖 Siber Güvenlik Test Laboratuvarı Aktif!\n".encode("utf-8"))

# Sitenin yerel bilgisayarınızda çalışacağı port (Varsayılan: 8080)
def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, TestServer)
    print("🚀 Test sitesi kodları hazır! Port 8080 dinleniyor...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

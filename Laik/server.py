# server.py
import http.server
import socketserver

def start_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    # Server starten
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Webserver läuft auf http://localhost:{PORT}")
        httpd.serve_forever()

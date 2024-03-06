from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

hostName = "localhost"
serverPort = 8080


class IntelligenceServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h3>Click <a href='http://localhost:8080/classify-image'>here</a> to classify image</h3>", "utf-8"))
        self.wfile.write(bytes("<h3>Click <a href='http://localhost:8080/extract-feature'>here</a> to extract image feature</h3>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

        if self.path == '/classify-image':
            print("classify-image called")
        elif self.path == '/extract-feature':
            print("extract-feature called")
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        if self.path.endswith('/classify-image'):
            print("classify-image called")
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                print("Body of data sent via http (POST) request: ", fields)
                image_url = fields.get('image-url')
                print("image-url is => " + image_url[0])
                self.end_headers()
                json_str = "{'result': 1}"
                self.wfile.write(bytes(json_str, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), IntelligenceServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

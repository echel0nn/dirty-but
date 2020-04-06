import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("192.168.56.1", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

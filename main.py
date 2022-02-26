import SocketServer
import socket
import sipproxy as proxy

if __name__ == "__main__":    
    print('Starting sip proxy')
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, proxy.PORT)
    proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, proxy.PORT)
    server = SocketServer.UDPServer((proxy.HOST, proxy.PORT), proxy.UDPHandler)
    print('Running...')
    server.serve_forever()
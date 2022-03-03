import SocketServer
import socket
import sipproxy as proxy

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == "__main__":    
    print('Starting sip proxy')
    ip_address = get_ip_address()
    proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ip_address, proxy.PORT)
    proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ip_address, proxy.PORT)
    server = SocketServer.UDPServer((proxy.HOST, proxy.PORT), proxy.UDPHandler)
    print('Running...')
    server.serve_forever()
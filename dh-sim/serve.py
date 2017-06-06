import socketserver
from connect import Packet


client_list = []

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        packet = self.parse_data_to_packet(self.data)
        if packet == -1:
            self.request.sendall("Malformed packet received")        

    def parse_data_to_packet(self):
        # TODO : place decryption here
        fields = self.data.split('/')
        if len(fields) != 4:
            return -1
        sender = fields[0]
        message = fields[1]
        target = fields[2]
        protocol = int(fields[3], 16)
        if protocol == 0:
            client_list.append(sender)
            to_send = Packet(target, '1', sender, 0)

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9998
    server = socketserver.TCPServer((HOST, PORT), Server)
    server.serve_forever()
    

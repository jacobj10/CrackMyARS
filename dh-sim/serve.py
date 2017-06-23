import socketserver
from connect import Packet


client_list = []

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        packet = self.parse_data_to_packet()
        if packet == -1:
            self.request.sendall(b'Malformed packet received')
        if  packet == -2:
            self.request.sendall(b'Invalid protocol received')

    def parse_data_to_packet(self):
        # TODO : place decryption here
        fields = self.data.decode('utf-8').split('/')
        if len(fields) != 4:
            return -1
        sender = fields[0]
        message = fields[1]
        target = fields[2]
        protocol = int(fields[3], 16)
        if protocol == 0:
            if sender in client_list:
                return -2
            print("{0} has joined the server".format(sender))
            client_list.append(sender)
            self.request.send(b'1')
        if protocol == 1:
            if sender not in client_list:
                return -2
            print("{0} has left the server".format(sender))
            client_list.remove(sender)

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9998
    server = socketserver.TCPServer((HOST, PORT), Server)
    server.serve_forever()
    

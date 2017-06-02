import random

class Client:
    def __init__(self, _id):
        self.id = _id
        self.my_secrets = {}
        self.our_secrets = {}
        self.server = None

    def send(self, info, target):
        mess = Packet(info, target, self.id)
        mess.send()

    def send_secret_req(self, target):
        self.my_secrets[target] = random.randint(1, 20000)
        self.our_secrets[target] = [23, 5]

    def recv(self, msg):
        print(_id + ' received a message')

class Packet:
    def __init__(self, content, target, sender):
        self.sender = sender
        self.content = content
        self.target = target

    def send(self):
        print("{0} -> {1}: {2}".format(self.sender, self.target, self.content))

class Server:
    def __init__(self, clients):
        self.clients = clients

    def send(msg, sender, target):
        packet.sender.send(msg, target)
        packet.target.recv(msg)
        
if __name__ == '__main__':
    alice = Client('alice')
    bob = Client('bob')
    clients = {'alice': alice, 'bob': bob}
    server = Server(clients)
    alice.server = server
    bob.server = server
    

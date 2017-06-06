import random
import binascii

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

    def connect(self, server):
        self.server = server
        send_packet = Packet("Connecting", server.id, self.id, 0) 
        send_packet.send()

class Packet:
    def __init__(self, content, target, sender, protocol):
        self.sender = sender
        self.content = content
        self.target = target
        self.protocol = protocol

    def to_string(self):
        to_send = "{0}/{1}/{2}/{3}".format(
                                        str(binascii.b2a_hex(str.encode(self.sender)), 'ascii'),
                                        str(binascii.b2a_hex(str.encode(self.content)), 'ascii'),
                                        str(binascii.b2a_hex(str.encode(self.target)), 'ascii'),
                                        hex(self.protocol)
                                    )
        return to_send

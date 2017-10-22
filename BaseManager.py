import time
import threading
import queue
from Packet import Packet

class BaseManager:

    def __init__(self):
        self.in_q = queue.Queue()
        self.out_q = queue.Queue()
        self.run_mgr = True;
        self.callback_dict = {}
        
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.start()

    def run(self):
        while self.run_mgr:
            packet = self.check_queue()
            if packet:
                if id(packet) in self.callback_dict.keys():
                    self.callback_dict[id(packet)](packet)
                else:
                    self.process_data(packet)
            else:
                pass

        return

    def end_mgr(self):
        self.run_mgr = False

    def check_queue(self):
            if not self.in_q.empty():
                return self.in_q.get()

    def send_packet(self,packet):
        self.out_q.put(packet)

    def send_data(self,receiver, message, data):
        packet = Packet()
        packet.receiver = receiver
        packet.data = data
        packet.message = message
        self.out_q.put(packet)

    def return_packet(self,packet):
        temp = packet.receiver
        packet.receiver = packet.sender
        packet.sender = temp
        self.out_q.put(packet)

    def send_async_packet(self, packet, callback):
        self.callback_dict[id(packet)] = callback
        self.send_packet(packet)

    def process_data(self,packet):
        raise NotImplementedError('You need to define a process_data method!')



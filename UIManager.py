import threading
import time
from BaseManager import BaseManager
from User import User
from Packet import Packet

class UIManager(BaseManager):
    def __init__(self):
        super().__init__()

        temp = User()

        packet = Packet()
        packet.receiver = "DataProcessingManager"
        packet.data = temp

        self.send_async_packet(packet,self.callback)

    def process_data(self,packet):
        data = packet.data
        print("UIManager received data: ", data.name)
        data.name = "Garrett"
        self.return_packet(packet)


    def callback(self,packet):
        data = packet.data
        print("Callback function received data:", data.name)


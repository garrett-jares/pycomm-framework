import time
import threading
from BaseManager import BaseManager
from User import User

class DataProcessingManager(BaseManager):

    def process_data(self,packet):
        print("DataProcessingManager received data: ", packet.data.name)
        packet.data.name = "Jen"
        self.return_packet(packet)


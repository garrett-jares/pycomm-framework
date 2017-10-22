import queue
import threading

class CommManager:
    def __init__(self):
        self.mgr_dict = {}
        self.run_comm = True
        
        thread = threading.Thread(target=self.run, args=())
        thread.start()                                  # Start the execution

    def add_manager(self,mgr,mgr_name):
        self.mgr_dict[mgr_name] = mgr
        
    def send_data(self,mgr_name,data):
        self.mgr_dict[mgr_name].in_q.put(data)

    def check_mgrs(self):
        for mgr_name, mgr in self.mgr_dict.items():
            if not mgr.out_q.empty():
                packet = mgr.out_q.get()

                receiver = packet.receiver
                packet.sender = mgr_name
                
                self.send_data(receiver, packet)

    def run(self):
        while self.run_comm:
            if self.mgr_dict:
                self.check_mgrs()
            else:
                pass

        self.kill_managers()
        return

    def kill_managers(self):
        for mgr in self.mgr_dict.values():
            mgr.end_mgr()
            mgr.thread.join()

    def end_comm(self):
        self.run_comm = False














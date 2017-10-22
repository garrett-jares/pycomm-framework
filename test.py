import UIManager
import DataProcessingManager
import time
from CommManager import CommManager

comm_mgr = CommManager()
x = UIManager.UIManager()
y = DataProcessingManager.DataProcessingManager()

comm_mgr.add_manager(x,"UIManager")
comm_mgr.add_manager(y,"DataProcessingManager")

input("Press Enter to continue...")
comm_mgr.kill_managers()
comm_mgr.end_comm()

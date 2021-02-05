import os
from .dependencies import InstallDep
import subprocess
class Update():
    def __init__(self, size,commands,):
        self.size = size
        self.commands = commands
    def upubuntu(self):
        #Get commands for dictionary for update
        comm = [self.commands["update"] for key in self.commands][0]
        cnt = 1
        print("*"*int(self.size[0]))
        print("1- Updating system".upper().center(int(self.size[0])))
        # Read each comamnd and execute
        for key,cmd in comm.items():
            print(f"1.{cnt}- {key}....")
            try:
                #Execute each command
                subprocess.check_output(cmd,shell=True)
                cnt +=1 
                if len(comm) == cnt:
                    print("!Update Complete!")
                    idp = InstallDep(self.size,self.commands)
                    idp.install()
            except Exception as e:
                #Show an error if command dont work
                print(f"ERROR: {e}")
                break
           
                   
    

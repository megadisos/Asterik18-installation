import os
import subprocess
from .build import 
class InstallDep():
    def __init__(self,size,command):
        self.size = size
        self.commands = command
    def install(self):
        cnt = 1
          #Get commands for dictionary for dependencies
        comm = [self.commands["dependencies"] for key in self.commands][0]
        print("*"*int(self.size[0]))
        print("2- Dependencies Installation".upper().center(int(self.size[0])))
         # Read each comamnd and execute
        for key,cmd in comm.items():
            print(f"1.{cnt}- {key}....")
            try:
                #Execute each command
                subprocess.check_output(cmd,shell=True)
                cnt +=1 
                if len(comm) == cnt:
                    print("!Installation Complete!")
            except Exception as e:
                #Show an error if command dont work
                print(f"ERROR: {e}")
                break
           
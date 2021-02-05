import os
import subprocess

class BuildAsterisk():
    def __init__(self,size,command):
        self.size = size
        self.command = command
    def downloadfiles(self):
        cnt = 1
        #Get commands for dictionary for update
        comm = [self.command["download"] for key in self.command][0]
        print("*"*int(self.size[0]))
        print("3- Asterisk Download".upper().center(int(self.size[0])))
        os.chdir(os.environ['HOME'])
        for key,cmd in comm.items():
            print(f"1.{cnt}- {key}....")
            try:
                if "Download mp3 decoder" in key:
                    os.chdir(os.path.join(os.environ['HOME'],"asterisk-18"))
                subprocess.check_output(cmd,shell=True)
                cnt+=1
                if len(comm) == cnt:
                    print("!The files were downladed!")
            except Exception as e:
                #Show an error if command dont work
                print(f"ERROR: {e}")

    def build(self):
        self.downloadfiles()
        comm = [self.command["build"] for key in self.command][0]
        print("*"*int(self.size[0]))
        print("4- Asterisk build".upper().center(int(self.size[0])))
        for key,cmd in comm.items():
            print(f"1.{cnt}- {key}....")
            try:
                subprocess.check_output(cmd,shell=True)
                cnt+=1
                if len(comm) == cnt:
                    print("!The Installation was completed")
            except Exception as e:
                #Show an error if command dont work
                print(f"ERROR: {e}")
        

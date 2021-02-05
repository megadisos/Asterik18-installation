from files.update import Update
from files.dependencies import InstallDep
import os

# Terminal Size
SIZE = os.get_terminal_size()
# Dictionary with commands to be used
COMMANDS_DICT = {
    "update":{"Updating Ubuntu":"sudo apt update",
              "Upgrading Ubuntu":"sudo apt -y upgrade"},
    "dependencies": {"Adding universe repository":"sudo add-apt-repository universe",
                    "Installing git,curl,sqllite,xml2":"sudo apt -y install git curl wget libnewt-dev libssl-dev libncurses5-dev subversion libsqlite3-dev build-essential libjansson-dev libxml2-dev  uuid-dev",
                    },
    "download": {"Downloading Asterisk 18":"wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz",
                "Extracting the file":"tar xvf asterisk-18-current.tar.gz",
                "Download mp3 decoder":"contrib/scripts/get_mp3_source.sh",
                "Ensure all dependencies are resolved":"sudo contrib/scripts/install_prereq install"},
    "build": {"Configuring scripts":"./configure",
               "Setting up menu options":"make menuselect",
               "Building Asterisk": "make",
               "Installing Aterisk": "sudo make install",
               "Documentation Installation":"sudo make progdocs",
               "Samples installation":"sudo make samples",
               "Install configs":"sudo make config",
               "Install configs p.2": "sudo ldconfig"
            },
                       
    }
# Main message
print("")
print("*"*int(SIZE[0]))
print("Asterisk 18 LTS installation on Ubuntu 20.04".upper().center(int(SIZE[0])))
print("*"*int(SIZE[0]))
print("Welcome:")
while True:
    op = input("Do you want to update and upgrade Ubuntu? Yes/No ")
    if op.lower() == "yes" or op.lower().startswith("y") :
        # Go to Update class to Update the system
        start = Update(SIZE,COMMANDS_DICT)
        start.upubuntu()
        break
    elif op.lower() == "no" or op.lower().startswith("n"):
        # Go to dependencies class to Install those without update
        start = InstallDep(SIZE,COMMANDS_DICT)
        start.install()
        break
    else:
        print("ERROR: Wrong option, must choose Yes or No")


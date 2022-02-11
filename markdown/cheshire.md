# Cheshire Webserver Manual

| Index | Technology | Info |
| ------ | ------ | ------ |
| 0 | Cisco VPN  | A Mac/Win program necessary for connection to UB Cheshire Linux Web Server |
| 1 | Filezilla  | A Mac/win program necessary for transferring files to/from UB Cheshire     | 
| 2 | SSH / Putty | A (Safe Secure Host) protocol to connect to remote servers. Putty is for windows    | 
| 3 | Bash   Env | A shell environment necessary for running python code and environments   |
| 4 | Python Venv | An isolated environment to run and install python code and pacakages  | 
| 5 | Crontab    | A CLI (command line utility), necessary for scheduling code automatically on Chesire  | 


&nbsp;

---
## 0 : Cisco VPN
---

By default, all of Cheshire's access can onlt be accessed locally on campus.  If you're not at UB, you will need this vpn to access the Cheshire terminal or transfer files with Filezilla. 



> NOTE: This theme of having network access is present throughout the entire technology stack

&nbsp;

#### General Steps 
  - Download [WIN](https://www.buffalo.edu/ubit/service-guides/software/downloading/windows-software/managing-your-software/anyconnect.html) : [MAC](https://www.buffalo.edu/ubit/service-guides/software/downloading/macintosh-software/managing-mac-software/anyconnect.html)

- Follow this guide (general steps also below)
  https://www.buffalo.edu/ubit/service-guides/connecting/vpn/computer.html
  1.  Enter into _URL_
      - vpn.buffalo.edu/UBVPN
  2. Enter into _Group_ 
      - UBVPN
  3.  Enter into _Username_ and _Password_ 
      - UB email (username)
      - UB email password
  4.  Type 1 or 2, into Duo Device and press enter 
      - will launch duo authenticator on phone
  5.  After you will be connected

&nbsp;

---
## 1 : Filezilla 
---

Filezilla is an SFTP Program (Secure File Transfer Protocol), that works well with file transferring for UB Cheshire



> NOTE: you must be on campus or be using the Cisco VPN

&nbsp;

#### General Steps 
- Download the program -> [WIN + MAC](https://filezilla-project.org/download.php?show_all=1)

- Connection Guide (general steps below)
  1. Enable all permissions when asked (for storage)
  2. Under the top navigation bar enter into _"HOST"_ _"PASSWORD"_ and _"PORT"_
      - <YOUR_UBIT_NAME>@cheshire.cse.buffalo.edu
      - <YOUR_UB_EMAIL_PASSWORD>
      - 22
  3. Unknown host key prompt will come up
      - check "always trust this host, add key to cache"
      - click ok
  4. Once connected, you can drag and drop files 
      - left side is your computer
      - right side is cheshire
  5. Important directories (note original path is different home vs web)
      - your home   -> /home/cendue/<YOUR_UBIT_NAME>
      - our project -> /web/woo_warehouse

&nbsp;

---
## 2. SSH Command  (Linux/Mac)
---

This is the command to connect to UB Cheshire and use the linux environment


> NOTE: you must be on campus or be using the Cisco VPN

&nbsp;


```
ssh <YOUR_UBIT_USERNAME>@cheshire.cse.buffalo.edu
```
- after enter your UBIT Passord (youw will not see cursor moving, that's ok)
- press enter 
- accept any RSA key permissions

&nbsp;

---
## 2.5 : Putty (SSH for Windows)
---

This is the same as above, but for a special program for windows



> NOTE: you must be on campus or be using the Cisco VPN

&nbsp;
```
<YOUR_UBIT_USERNAME>@cheshire.cse.buffalo.edu
```
- enter the above into HOST and your email password into PASSWORD
- enter 22 for port
- accept any RSA key permissions

&nbsp;

---
## 3 : Bash Environment 
---

Bash is the shell to create a script environment to run code flexibly without interacting with UB's core admininstrative features

> NOTE: you will not be able to run any python code if not in bash 

&nbsp;
### CLI Directory and File Examples 
```
bash                  # starts bash
pwd                   # shows current directory
mkdir exampe_folder   # makes directory 
cd /example_folder    # change directory (into sub folder)
cd ..                 # change directory (move parent folder)

touch example.py      # creates empty text file (any extention)
nano example.py       # opens nano text editor on new/existing file 

cp example.py exampleCopy.py        # copies file
mv exampleCopy.py newExample.py     # changes name of file

rm example.py         # removes single file
rm -r example_folder  # removes folder and all items inside 

exit                  # closes bash
```


### Editing and setting a new/existing profile
```
nano ~/.bashrc       # will open editor to type or paste commands
source ~/.bashrc     # will reset shell with new commands
```

### Custom commands for ~/.bashrc
```
# Below are all custom shortcut commands #

alias public='source /web/woo_warehouse/venv/bin/activate; cd ~/public_html'
alias woo='source /web/woo_warehouse/venv/bin/activate; cd /web/woo_warehouse'
alias cron='source /web/woo_warehouse/venv/bin/activate; cd /web/woo_warehouse/cron'
```

&nbsp;

---
## 4. Python Virtual Environment 
---
This is the only way to install and use modules from the python pip package manager.  The virutal environment for this project is using 3.8.12

> NOTE: You cannot move this environment once created as the path is deep linked into the environment.  Build a requirements.txt (pip freeze > requirements.txt) and install modules for each virtual environment

> NOTE: Python3 and pip commands are available after creating and activating the venv.  Crontab also must activate this venv

&nbsp;
### VENV example
```
/util/python-3.8.1/bin/python3 -m venv YOUR_VENV_NAME    # create the venv
bash /YOUR_VENV_NAME/bin/activate                        # activate the venv
deactivate                                               # deactivate the venv
```

&nbsp;

---
## 5. Crontab Scheduler
---
This is the only way to launch scripts and code automatically outsie of the terminal

> WARNING: Once a script is ran in the crontab, the only output you'll see are the terminal logs sent to your UB email. 

> WARNING: Once you run a script with the crontab, you cannot cancel the script without calling or emailing the IT dept.  This is due to students not being able to kill linux processes.


&nbsp;
### Open Crontab
  - You will be prompted to pick a CLI text editor (vim, nano, emacs)
  - Then you will be directed to the editor you chose 
  - Scheduler will set once you saved and exited the editor
```
crontab -e    # launches the crontab editor
```

### Example Crontab Template
  - For our project, each python script is wrapped in a bash .sh script
  - This is because there are too many terminal commands to change directories and use the virutal environment
  - Below is an example of our project's cron setup 
  - Lines can be commented out since cron itself is a bash script

```
# TEST   ==============================
# * * * * * bash ~/DEV/TEST.sh                        # Every minute

# STABLE ==============================
10 10 * * 1-5 bash /web/woo_warehouse/cron/DAILY.sh   # Every 10:10am Mon-Fri
0 */4 * * * bash /web/woo_warehouse/cron/WPS.sh       # Every 4 hours Mon-Fri
0 */4 * * * bash /web/woo_warehouse/cron/CHARLES.sh   # ^^^
0 */1 * * * bash /web/woo_warehouse/cron/main.sh      # ^^^

# BETA   ==============================
0 9 * * 1-5  bash /web/woo_warehouse/cron/streamer.sh       # Every 9am Mon-Fri
30 10 * * 1-5  bash /web/woo_warehouse/cron/recommender.sh  # Every 10:30am Mon-Fri
```

import os, subprocess
import re
import sys
import string
import paramiko
from threading import Timer
#import schedule
import time
from time import strftime
import shutil
from cryptography.fernet import Fernet


x_file = open('/home/netops/script_key', 'r').read()

y_file = open('/home/netops/encrypt_val', 'r').read()

cipher_suite=Fernet(x_file)

host_ip = '<ip of firewall>'
login_username = 
login_password = 

##Below Commands will create a file with the date and time and store it in the specifiedm location##

moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())

save_path = '/usr/local/bin/snapshot_dump/Walnut_Creek/USCAWCFW1/USCAWCFW1_show_arp.py/'

name_of_file="sh_arp_<ip of firewall>"

completeName = os.path.join(save_path,name_of_file)
file1 = open(completeName+moment+'.log', "w")

##Below lines of code will Connect to the ASA and execute the specified command##

client_pre=paramiko.SSHClient()
client_pre.load_system_host_keys()
client_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_pre.connect(host_ip, username=login_username , password=login_password, look_for_keys=False, allow_agent=False)

client=client_pre.invoke_shell()
time.sleep(2)
output=client.recv(65535)
#print (output.splitlines())

client.send('terminal pager 0\n')
time.sleep(2)
output=client.recv(65535)
print(output.splitlines())

client.send('show arp\n')
time.sleep(2)
version_info = ""
output = " "


while client.recv_ready():
 output = client.recv(1)
 version_info += output.decode('UTF-8')

file1.write(version_info)
client.close()
client_pre.close()

##

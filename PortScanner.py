import socket
import sys
import threading
from termcolor import colored

def banner(host ,port):
    data = s.connect((host ,port))
    return data.recv(1024)

print('\n >                   Robocodemore Port Scanner \n' + '=' * 67 + '\n')

if len(sys.argv) > 1:
	target = socket.gethostbyname(sys.argv[1])
	print('Enter target: ' + target)

else:
	target = socket.gethostbyname(input('Enter target: '))


def scanPort(target, port):
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)

	c = s.connect_ex((target, port))
	if c == 0:
		try:
		    data = banner(target ,port)
		    print(colored('' + target + '~Port: [open] ' + str(port, ) + data ,'green'))
		    s.close()
		    
		except Exception as err:
		    #print(err)
		    print(colored('' + target + '~Port: [open] ' + str(port, ) ,'green'))
def main():
    for i in range(1, 1024):
        scan = threading.Thread(target=scanPort, args=(target, i))
        scan.start()   

main()

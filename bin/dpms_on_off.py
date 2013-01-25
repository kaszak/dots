#!/usr/bin/env python

import re
from subprocess import Popen, call, PIPE
import sys
import socket

dpms_re = re.compile(r'DPMS is (?P<state>Enabled|Disabled)')
command_q = 'xset q'.split()
command_off = 'xset -dpms; xset s off'
command_on = 'xset +dpms; xset s on'
command_dpms_off = 'xset dpms force off'

def send_to_statusbar(state, port):
    send_state = socket.socket()
    send_state.connect(('localhost', port))
    send_state.sendall(state)
    send_state.close()

def main():
    '''
    Turns off screen power management if it's on, otherwise turns it
    on. Can also turn off backlight.
    '''
    
    with open('/tmp/.statusbar.port') as port_file:
        port = int(port_file.read())
    if len(sys.argv) <= 1:
        xset = Popen(command_q, stdout=PIPE)
        output = xset.stdout.read().decode()
        dpms_state = dpms_re.search(output).group('state')
        if dpms_state == 'Enabled':
            call(command_off, shell=True)
            state = b'OFF'
        else:
            call(command_on, shell=True)
            state = b'ON'
    elif sys.argv[1] == 'off':
        call(command_dpms_off, shell=True)
        state = b'ON'
        
    send_to_statusbar(state, port)
        
	

if __name__ == '__main__':
	main()

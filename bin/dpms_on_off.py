#!/usr/bin/env python

import re
from subprocess import Popen, call, PIPE

dpms_re = re.compile(r'DPMS is (?P<state>Enabled|Disabled)')
command_q = 'xset q'.split()
command_off = 'xset -dpms; xset s off'
command_on = 'xset +dpms; xset s on'

def main():
    '''Turns off screen power management if it's on, otherwise turns it
    on.'''
    xset = Popen(command_q, stdout=PIPE)
    output = xset.stdout.read().decode()
    
    dpms_state = dpms_re.search(output).group('state')
    if dpms_state == 'Enabled':
        call(command_off, shell=True)
    else:
        call(command_on, shell=True)
	

if __name__ == '__main__':
	main()

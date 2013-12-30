######################################
##  This is a wrapper class to      ##
##  Have common access to the GPIO  ##
##  Interface of the Resberry Pi    ##
##                                  ##
##  Brendon Malachi                 ##
##  Code referrance from:           ##
##  https://pypi.python.org/pypi/RPi.GPIO
######################################

#!/usr/bin/python
LocalPath = r'/home/pi/Script'
from sys import path
if  not in path:
    path.append(LocalPath)
    
''' This will be used to test our IR sensor'''

try:
    import GPIOWrapperClass as GPIO
    import WiringExtenstionBoard as  ExtenBoard
    print 'Loaded the GPIO Wrapper'
except RuntimeError:
    print"Error importing GPIO Wrapper!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script"

# Making this object a global
GPIOWrp = None

if __name__=='__main__':
    print '*'*RowLen
    print 'Running localy on this file=%s' % 'need to replace to __file__'
    print '*'*RowLen
    print '\n'*RowSpace

    
    pin_mode='BOARD'
    warning_level=False
    WireBoardWrp = ExtenBoard.clsWiringExtenstionBoard()
    global GPIOWrp
    GPIOWrp = GPIO.clsGPIOWrapper(pin_mode, warning_level)
    pin = eval('WireBoardWrp.PortMapDict[\'P7\']')
    GPIOWrp.GPIOSetUp(pin, 'in', None, None)

    while(True):
        Menu = raw_input('Press Enter for \'NOP\', \'q\' to quit >>> Input: ')
        if Menu.lower() in ['q', 'quit']:
            break
  
    del GPIOWrp
    del WireBoardWrp

    print '\n'*RowSpace
    print '*'*RowLen
    print 'Ending local run'
    print '*'*RowLen

    

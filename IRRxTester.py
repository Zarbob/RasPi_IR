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
if LocalPath not in path:
    path.append(LocalPath)

# For debug usage
from time import sleep, clock, time
import pdb

''' This will be used to test our IR sensor'''

#Local var's
RowLen=56
RowSpace=2

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

    tick=0
    tock=0
    Counter=0
    
    def cbRedButtonPress(Ch):
        print 'Red Button got pressed'
        global tick
        global tock
        global Counter
        print 'Clear time counter'        
        tick=0
        tock=0
        Counter=0
        
    def cbYellowButtonPress(Ch):
        print 'Yellow Button got pressed'

    def cbIRToggle(Ch):
        #http://www.sbprojects.com/knowledge/ir/nec.php
        global tick
        global tock
        global Counter
        tock = time()
##        tock = clock()                
        Counter+=1
        Diff = (tock-tick)*1e3
        if Diff>30:
            Val='End'
        elif Diff>7:
            Val ='AGC'
        elif Diff>3.5:
            Val='Space'
        elif Diff>1 and Diff<2:
            Val=1
        else:
            Val=-9999
        print 'IR toogle #%d, time Diff=%f [mSec], Bit=%d' %(Counter, Diff, Val)
        tick = tock
        
    pin_mode='BOARD'
    warning_level=False
    WireBoardWrp = ExtenBoard.clsWiringExtenstionBoard()
    global GPIOWrp
    GPIOWrp = GPIO.clsGPIOWrapper(pin_mode, warning_level)
    RedButt = eval('WireBoardWrp.PortMapDict[\'P7\']')
    YellowButt = eval('WireBoardWrp.PortMapDict[\'P6\']')
    GPIOWrp.GPIOSetUp(RedButt, 'in', None, None)
    GPIOWrp.GPIOSetUp(YellowButt, 'in', None, None)
    GPIOWrp.AddEvent('RedButt', RedButt, GPIOWrp.RISING, cbRedButtonPress, 200)
    GPIOWrp.AddEvent('YellowButt', YellowButt, GPIOWrp.RISING, cbYellowButtonPress, 200)

    IRRx = eval('WireBoardWrp.PortMapDict[\'P5\']')
    GPIOWrp.GPIOSetUp(IRRx, 'in', 'down', 'low')
    GPIOWrp.AddEvent('IRRx', IRRx, GPIOWrp.BOTH, cbIRToggle, None)

    t1=time()
    t2=time()
    print 'Quick time check, t1=%f, t2=%f, time diff %f[uSec]' %(t1, t2, (t2-t1)*10e6)
    
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

    

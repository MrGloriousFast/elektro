'''
General notes:

gpio pins i have hardware wired into the breadboard:
5 6 12 13 16 19 20 21 23 24 26

command line command should look like this:

powerplug 1 on
powerplug 2 off
powerplug 4 off
powerplug 3 on
powerplug all on
powerplug all off

'''
import RPi.GPIO as GPIO
import time

button_on  = {}
button_off = {}

def init_gpio():
    # i dont know what this does but it was in a tutorial
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # mapping of gpio pin number and the powerplug button number
    # there are 10 buttons in total
    # button 5 is the 'all on' or the 'all off' button on the remote
    button_on[1]  = 5
    button_on[2]  = 6
    button_on[3]  = 12
    button_on[4]  = 13
    button_on[5]  = 16
    button_off[1] = 19
    button_off[2] = 20
    button_off[3] = 21
    button_off[4] = 23
    button_off[5] = 24

    # set all gpio pins to output instead of input
    for buttons in (button_on.values(), button_off.values()):
        for b in buttons:
            GPIO.setup(b,GPIO.OUT)
            print 'gpio ' + str(b) + ' set to output'

#will press a button for one seconds
def press_button(button):
    # press it for one second
    GPIO.output(button,GPIO.HIGH)
    time.sleep(1)  
  
    # stop pressing it
    GPIO.output(button,GPIO.LOW)

def main():
    init_gpio()
    
    press_button(button_on[2])
    
if __name__ == "__main__":
    main()

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(27)
led2 = LED(17)
led3 = LED(18)

screen= Tk()
screen.title("LED TOGGLER")
def ledToggle1():
    ## for LED 1 ##
    if led1.is_lit:
        led1.off()
        RedLight["text"] =  "Turn LED 1 on"
        
    else:
        led1.on()
        led2.off()
        led3.off()
        RedLight["text"] =  "Turn LED 1 off"
        BlueLight["text"] =  "LED 2 is off"
        OrangeLight["text"] =  "LED 3 is off"
        
def ledToggle2():
      ## for LED 2 ##
    if led2.is_lit:
        led2.off()
        BlueLight["text"] =  "Turn LED 2 on"
        
    else:
        led2.on()
        led1.off()
        led3.off()
        BlueLight["text"] =  "Turn LED 2 off"
        RedLight["text"] =  "LED 1 is off"
        OrangeLight["text"] =  "LED 3 is off"

def ledToggle3():   
        ## for LED 3 ##
    if led3.is_lit:
        led3.off()
        ledButton3["text"] =  "Turn LED 3 on"
        
    else:
        led3.on()
        led2.off()
        led1.off()
        OrangeLight["text"] =  "Turn LED 3 off"
        RedLight["text"] =  "LED 1 is off"
        BlueLight["text"] =  "LED 2 is off"
    
def ledToggle4():
    
    led3.off()
    led2.off()
    led1.off()
    OrangeLight["text"] =  "LED 3 is off"
    RedLight["text"] =  "LED 1 is off"
    BlueLight["text"] =  "LED 2 is off"

def ledToggle5():
    
    led3.on()
    led2.on()
    led1.on()
    OrangeLight["text"] =  "LED 3 is on"
    RedLight["text"] =  "LED 1 is on"
    BlueLight["text"] =  "LED 2 is on"

def close():
    RPi.GPIO.cleanup()
    screen.destroy()
    
RedLight = Button(screen, text = "Turn LED 1 ", command =ledToggle1,bg = "blue", height = 1, width =20)
BlueLight = Button(screen, text = "Turn LED 2", command =ledToggle2,bg = "blue", height = 1, width =20)
OrangeLight = Button(screen, text = "Turn LED 3", command =ledToggle3,bg = "blue", height = 1, width =20)
OffLight = Button(screen, text = "Turn all LEDS Off", command =ledToggle4,bg = "blue", height = 1, width =20)
OnLight = Button(screen, text = "Turn all LEDS Off", command =ledToggle5,bg = "blue", height = 1, width =20)

RedLight.grid(row=0, column =1)
BlueLight.grid(row=1, column =1)
OrangeLight.grid(row=2, column =1)
OffLight.grid(row=3, column=1)
OnLight.grid(row=4, column=1)

exitButton = Button(screen, text = "EXIT", command = close, bg = "red", height =1 , width = 10)
exitButton.grid(row = 5, column = 1)

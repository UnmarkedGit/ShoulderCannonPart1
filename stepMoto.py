
#   WORKING FOR X Motor
import RPi.GPIO as GPIO
import time, sys
 #LR Motor
out1 = 17
out2 = 18
out3 = 27
out4 = 22
 #UD Motor
out5 = 12
out6 = 16
out7 = 20
out8 = 21
 #Trigger Motor
out9 = 23
out10 = 24
out11 = 25
out12 = 8
 
#for left and right
RLstep_sleep = 0.002
 
#step_count =  100

#for up and down
UDstep_sleep = 0.01

step_count =  100

#Trigger
TrigStep_sleep = 0.002

TrigStep_count =  4096

 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( out1, GPIO.OUT )
GPIO.setup( out2, GPIO.OUT )
GPIO.setup( out3, GPIO.OUT )
GPIO.setup( out4, GPIO.OUT )

GPIO.setup( out5, GPIO.OUT )
GPIO.setup( out6, GPIO.OUT )
GPIO.setup( out7, GPIO.OUT )
GPIO.setup( out8, GPIO.OUT )

GPIO.setup( out9, GPIO.OUT )
GPIO.setup( out10, GPIO.OUT )
GPIO.setup( out11, GPIO.OUT )
GPIO.setup( out12, GPIO.OUT )
 
# initializing
GPIO.output( out1, GPIO.LOW )
GPIO.output( out2, GPIO.LOW )
GPIO.output( out3, GPIO.LOW )
GPIO.output( out4, GPIO.LOW )
 
GPIO.output( out5, GPIO.LOW )
GPIO.output( out6, GPIO.LOW )
GPIO.output( out7, GPIO.LOW )
GPIO.output( out8, GPIO.LOW )

GPIO.output( out9, GPIO.LOW )
GPIO.output( out10, GPIO.LOW )
GPIO.output( out11, GPIO.LOW )
GPIO.output( out12, GPIO.LOW )

righti = 0
lefti = 0
upi = 0
downi = 0
 
def cleanup():
    GPIO.output( out1, GPIO.LOW )
    GPIO.output( out2, GPIO.LOW )
    GPIO.output( out3, GPIO.LOW )
    GPIO.output( out4, GPIO.LOW )
    GPIO.output( out5, GPIO.LOW )
    GPIO.output( out6, GPIO.LOW )
    GPIO.output( out7, GPIO.LOW )
    GPIO.output( out8, GPIO.LOW )
    GPIO.output( out9, GPIO.LOW )
    GPIO.output( out10, GPIO.LOW )
    GPIO.output( out11, GPIO.LOW )
    GPIO.output( out12, GPIO.LOW )
    GPIO.cleanup()

def rightTurn():
    global righti
    i = 0
    for i in range(50):
        if righti%4==3:
            GPIO.output( out4, GPIO.HIGH )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif righti%4==2:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.HIGH )
            GPIO.output( out1, GPIO.LOW )
        elif righti%4==1:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.HIGH )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif righti%4==0:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW ) 
            GPIO.output( out1, GPIO.HIGH )
 
        righti=righti+1
        
        time.sleep( RLstep_sleep )
    
def leftTurn():
    global lefti
    i = 0
    for i in range(10):
        if lefti%4==0:
            GPIO.output( out4, GPIO.HIGH )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif lefti%4==1:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.HIGH )
            GPIO.output( out1, GPIO.LOW )
        elif lefti%4==2:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.HIGH )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif lefti%4==3:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.HIGH )
        lefti=lefti+1
 
        time.sleep( RLstep_sleep )
    
def downTurn():
    global downi
    i = 0
    for i in range(25):
        if downi%4==0:
            GPIO.output( out8, GPIO.HIGH )
            GPIO.output( out7, GPIO.LOW )
            GPIO.output( out6, GPIO.LOW )
            GPIO.output( out5, GPIO.LOW )
        elif downi%4==1:
            GPIO.output( out8, GPIO.LOW )
            GPIO.output( out7, GPIO.LOW )
            GPIO.output( out6, GPIO.HIGH )
            GPIO.output( out5, GPIO.LOW )
        elif downi%4==2:
            GPIO.output( out8, GPIO.LOW )
            GPIO.output( out7, GPIO.HIGH )
            GPIO.output( out6, GPIO.LOW )
            GPIO.output( out5, GPIO.LOW )
        elif downi%4==3:
            GPIO.output( out8, GPIO.LOW )
            GPIO.output( out7, GPIO.LOW )
            GPIO.output( out6, GPIO.LOW )
            GPIO.output( out5, GPIO.HIGH )
        downi=downi+1
 
        time.sleep( UDstep_sleep )
    
def upTurn():
    global upi
    i = 0
    for i in range(25):
        if upi%4==3:
            GPIO.output( out8, GPIO.HIGH )
            GPIO.output( out7, GPIO.LOW )
            GPIO.output( out6, GPIO.LOW )
            GPIO.output( out5, GPIO.LOW )
        elif upi%4==2:
            GPIO.output( out8, GPIO.LOW )
            GPIO.output( out7, GPIO.LOW )
            GPIO.output( out6, GPIO.HIGH )
            GPIO.output( out5, GPIO.LOW )
        elif upi%4==1:
            GPIO.output( out8, GPIO.LOW )
            GPIO.output( out7, GPIO.HIGH )
            GPIO.output( out6, GPIO.LOW )
            GPIO.output( out5, GPIO.LOW )
        elif upi%4==0:
            GPIO.output( out8, GPIO.LOW )
            GPIO.output( out7, GPIO.LOW )
            GPIO.output( out6, GPIO.LOW )
            GPIO.output( out5, GPIO.HIGH )
        upi=upi+1
 
        time.sleep( UDstep_sleep )  

def TrigPush():
    i = 0
    for i in range(240):
        if i%4==3:
            GPIO.output( out9, GPIO.HIGH )
            GPIO.output( out10, GPIO.LOW )
            GPIO.output( out11, GPIO.LOW )
            GPIO.output( out12, GPIO.LOW )
        elif i%4==2:
            GPIO.output( out9, GPIO.LOW )
            GPIO.output( out10, GPIO.HIGH )
            GPIO.output( out11, GPIO.LOW )
            GPIO.output( out12, GPIO.LOW )
        elif i%4==1:
            GPIO.output( out9, GPIO.LOW )
            GPIO.output( out10, GPIO.LOW )
            GPIO.output( out11, GPIO.HIGH )
            GPIO.output( out12, GPIO.LOW )
        elif i%4==0:
            GPIO.output( out9, GPIO.LOW )
            GPIO.output( out10, GPIO.LOW )
            GPIO.output( out11, GPIO.LOW )
            GPIO.output( out12, GPIO.HIGH )
 
        time.sleep( TrigStep_sleep )

def TrigReturn():
    i = 0
    for i in range(240):
        if i%4==0:
            GPIO.output( out9, GPIO.HIGH )
            GPIO.output( out10, GPIO.LOW )
            GPIO.output( out11, GPIO.LOW )
            GPIO.output( out12, GPIO.LOW )
        elif i%4==1:
            GPIO.output( out9, GPIO.LOW )
            GPIO.output( out10, GPIO.HIGH )
            GPIO.output( out11, GPIO.LOW )
            GPIO.output( out12, GPIO.LOW )
        elif i%4==2:
            GPIO.output( out9, GPIO.LOW )
            GPIO.output( out10, GPIO.LOW )
            GPIO.output( out11, GPIO.HIGH )
            GPIO.output( out12, GPIO.LOW )
        elif i%4==3:
            GPIO.output( out9, GPIO.LOW )
            GPIO.output( out10, GPIO.LOW )
            GPIO.output( out11, GPIO.LOW )
            GPIO.output( out12, GPIO.HIGH )
 
        time.sleep( TrigStep_sleep )

while (1):
    x=sys.stdin.read(1)[0]
    if x == "a":
        leftTurn()
    if x == "d":
        rightTurn()
    if x == "w":
        upTurn()
    if x == "s":
        downTurn()
    if x == "f":
        TrigPush()
        TrigReturn()
    if x == "q":
        print("Pressed",x)
        cleanup()
        break


import RPi.GPIO as GPIO
import time

#set color

red_led = 23	#connect your red LED to pin 23
green_led = 18	#connect your green LED to pin 18
yellow_led = 24	#connect your yellow LED to pin 24

#set pins

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_led,GPIO.OUT)
GPIO.setup(green_led,GPIO.OUT)
GPIO.setup(yellow_led,GPIO.OUT)


#main

red = ["red","Red","RED","R","r"]
green = ["green","Green","GREEN","G","g"]
yellow = ["yellow","Yellow","YELLOW","Y","y"]
redgreen = ["redgreen","red green","Red Green","Redgreen","REDGREEN","RED GREEN","rg","RG"]
redyellow = ["redyellow","red yellow","Red Yellow","Redyellow","REDYELLOW","RED YELLOW","ry","RY"]
greenyellow = ["greenyellow","green yellow","Green Yellow","Greenyellow","GREENYELLOW","RED GREEN","rg","RG"]
redgreenyellow = ["redgreenyellow","red green yellow","REDGREENYELLOW","RedGreenYellow","Red Green Yellow","RGY","rgy"]

try:
	while True:
		color = input("Please select a color. (RED, GREEN, YELLOW)")
		if (color in red):
			GPIO.output(red_led,GPIO.HIGH)		#turns on the red LED
			GPIO.output(green_led,GPIO.LOW) 	#turns off the green LED
			GPIO.output(yellow_led,GPIO.LOW)	#turns off the yellow LED
			time.sleep(1) 						#wait 1 second
		elif (color in green):
			GPIO.output(red_led,GPIO.LOW)
			GPIO.output(green_led,GPIO.HIGH)
			GPIO.output(yellow_led,GPIO.LOW)
			time.sleep(1)
		elif (color in yellow):
			GPIO.output(red_led,GPIO.LOW)
			GPIO.output(green_led,GPIO.LOW)
			GPIO.output(yellow_led,GPIO.HIGH)
			time.sleep(1)
		elif (color in redgreen):
			GPIO.output(red_led,GPIO.HIGH)
			GPIO.output(green_led,GPIO.HIGH)
			GPIO.output(yellow_led,GPIO.LOW)
			time.sleep(1)
		elif (color in redyellow):
			GPIO.output(red_led,GPIO.HIGH)
			GPIO.output(green_led,GPIO.LOW)
			GPIO.output(yellow_led,GPIO.HIGH)
			time.sleep(1)
		elif (color in greenyellow):
			GPIO.output(red_led,GPIO.LOW)
			GPIO.output(green_led,GPIO.HIGH)
			GPIO.output(yellow_led,GPIO.HIGH)
			time.sleep(1)
		elif (color in redgreenyellow):
			GPIO.output(red_led,GPIO.HIGH)
			GPIO.output(green_led,GPIO.HIGH)
			GPIO.output(yellow_led,GPIO.HIGH)
			time.sleep(1)
		else:
			GPIO.output(red_led,GPIO.LOW)
			GPIO.output(green_led,GPIO.LOW)
			GPIO.output(yellow_led,GPIO.LOW)
			time.sleep(1)
except KeyboardInterrupt:	#press CTRL + C to exit
	GPIO.cleanup()
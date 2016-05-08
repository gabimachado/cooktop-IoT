#Authors: Gabriella Machado and Natalie Bezerra

import time
import datetime
import sqlite3
import os
import glob
import RPi.GPIO as GPIO
import httplib, urllib

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Initialize SQLite
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# GPIO Setup
GPIO.setmode(GPIO.BCM)
LIGHT_PIN1 = 18
LIGHT_PIN2 = 20
LIGHT_PIN3 = 21

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			temp_f = temp_c * 9.0 / 5.0 + 32.0
return temp_f
    
#Displays Temperature on ThingSpeak
def doit():
	params = urllib.urlencode({'field1': read_temp(), 'key'= 'API_KEY_NUMBER'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	data = response.read()
	conn.close()

# Get current mode from DB
def getCurrentMode():
	cur.execute('SELECT * FROM myapp_mode')
	data = cur.fetchone()  # (1, u'manual')
	return data[1]

# Get current state from DB
def getCurrentState():
	cur.execute('SELECT * FROM myapp_state')
	data = cur.fetchone()  # (1, u'on')
	return data[1]

# Store current state in DB
def setCurrentState(val):
	query = 'UPDATE myapp_state set name = "'+val+'"'
	cur.execute(query)

def switchOnLight(PIN):
	GPIO.setup(PIN, GPIO.OUT)
	GPIO.output(PIN, True)

def switchOffLight(PIN):
	GPIO.setup(PIN, GPIO.OUT)
	GPIO.output(PIN, False)

def runManualMode():
    # Get current state from DB
	currentState = getCurrentState()
	if currentState == 'low':
        	print 'Heating - Low'
        	switchOnLight(LIGHT_PIN1)
		switchOffLight(LIGHT_PIN2)
		switchOffLight(LIGHT_PIN3)
        
	elif currentState == 'medium':
		print 'Heating - Medium'
		switchOnLight(LIGHT_PIN1)
		switchOnLight(LIGHT_PIN2)
		switchOffLight(LIGHT_PIN3)

	elif currentState == 'high':
		print 'Heating - High'
		switchOnLight(LIGHT_PIN1)
		switchOnLight(LIGHT_PIN2)
		switchOnLight(LIGHT_PIN3)

	elif currentState == 'off':
		print 'Heating - Off'
		switchOffLight(LIGHT_PIN1)
		switchOffLight(LIGHT_PIN2)
		switchOffLight(LIGHT_PIN3)

def runAutoMode():
	currentMode = getCurrentMode()
	if read_temp() <= 77:
		msg = ("Temperature: " + str("%.2f" % read_temp()) + " " + u"\u2109")
		print msg
		switchOnLight(LIGHT_PIN1)
		switchOffLight(LIGHT_PIN2)
		switchOffLight(LIGHT_PIN3)

	elif 77 < read_temp() <= 80:
		msg = ("Temperature: " + str("%.2f" % read_temp()) + " " + u"\u2109")
		print msg
		switchOnLight(LIGHT_PIN1)
		switchOnLight(LIGHT_PIN2)
		switchOffLight(LIGHT_PIN3)

	elif 80 < read_temp() <= 81:
		msg = ("Temperature: " + str("%.2f" % read_temp()) + " " + u"\u2109")
		print msg
		switchOnLight(LIGHT_PIN1)
		switchOnLight(LIGHT_PIN2)
		switchOnLight(LIGHT_PIN3)

	elif read_temp() > 81:
		msg = ("Temperature: " + str("%.2f" % read_temp()) + " " + u"\u2109")
		print msg
		switchOffLight(LIGHT_PIN1)
		switchOffLight(LIGHT_PIN2)
		switchOffLight(LIGHT_PIN3)
	
# Controller main function
def runController():
	currentMode = getCurrentMode()
	if currentMode == 'manual':
		runManualMode()
	if currentMode == 'auto':
		runAutoMode()
		doit()
		time.sleep(1)
return True

while True:
	try:
		runController()
		time.sleep(2)
        
	except KeyboardInterrupt:
		GPIO.cleanup()       
		exit()

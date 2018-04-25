import random

def actuatortrigger(num,fpos,fneg):
	if num > 0:
		fpos(num)
	elif num < 0: 
		fneg(num)
	
def aircon(num):
	print "cooling down"
	
def heater(num):
	print "heating"
	
def hvac(thresh, sensorval):
	actuatortrigger(sensorval-thresh,aircon,heater)
	
def randomsensor ():
	return random.random() * 100
	
for t in range(10):
	sensorval = randomsensor()
	print "sensing", sensorval,
	hvac(70,sensorval)
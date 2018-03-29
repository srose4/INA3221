#!/usr/bin/env python
#
# Shawn Rose
# 2018
#
#

# imports
import csv
import time
import SDL_Pi_INA3221

CH1_RESISTOR_VALUE = 0.1  # 0.1 Ohm
CH2_RESISTOR_VALUE = 0.1  # 0.1 Ohm
CH3_RESISTOR_VALUE = 0.1  # 0.1 Ohm
CH1 = 1
CH2 = 2
CH3 = 3

timestr = time.strftime("%Y%m%d-%H%M%S")

CSV_FILE = timestr + ".csv"

def main():
	ina3221 = SDL_Pi_INA3221.SDL_Pi_INA3221(addr=0x40)

	with open(CSV_FILE, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['CH1 BUS V', 'CH1 SHUNT V', 'CH1 CURRENT mA', 
			'CH2 BUS V', 'CH2 SHUNT V', 'CH2 CURRENT mA', 
			'CH3 BUS V', 'CH3 SHUNT V', 'CH3 CURRENT mA'])

	while True:
		print "------------------------------"
	  	shuntvoltage1 = 0
	  	busvoltage1   = 0
	  	current_mA1   = 0

	  	busvoltage1 = ina3221.getBusVoltage_V(CH1)
	  	shuntvoltage1 = ina3221.getShuntVoltage_mV(CH1)
	  	current_mA1 = ina3221.getCurrent_mA(CH1, CH1_RESISTOR_VALUE)  
	  
	  	print "CH1 Bus Voltage: %3.2f V " % busvoltage1
	  	print "CH1 Shunt Voltage: %3.2f mV " % shuntvoltage1
	  	print "CH1 Current 1:  %3.2f mA" % current_mA1
	  	print

	  	shuntvoltage2 = 0
	  	busvoltage2   = 0
	  	current_mA2   = 0

	  	busvoltage2 = ina3221.getBusVoltage_V(CH2)
	  	shuntvoltage2 = ina3221.getShuntVoltage_mV(CH2)
	  	current_mA2 = ina3221.getCurrent_mA(CH2, CH2_RESISTOR_VALUE)  
	  
	  	print "CH2 Bus Voltage: %3.2f V " % busvoltage2
	  	print "CH2 Shunt Voltage: %3.2f mV " % shuntvoltage2
	  	print "CH2 Current:  %3.2f mA" % current_mA2
	  	print

	  	shuntvoltage3 = 0
	  	busvoltage3   = 0
	  	current_mA3   = 0

	  	busvoltage3 = ina3221.getBusVoltage_V(CH3)
	  	shuntvoltage3 = ina3221.getShuntVoltage_mV(CH3)
	  	current_mA3 = ina3221.getCurrent_mA(CH3, CH3_RESISTOR_VALUE)  
	  
	  	print "CH3 Bus Voltage: %3.2f V " % busvoltage3
	  	print "CH3 Shunt Voltage: %3.2f mV " % shuntvoltage3
	  	print "CH3 Current:  %3.2f mA" % current_mA3
	  	print

	  	with open(CSV_FILE, 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([busvoltage1, shuntvoltage1, current_mA1,
				busvoltage2, shuntvoltage2, current_mA2,
				busvoltage3, shuntvoltage3, current_mA3])

	  	time.sleep(2)

if __name__ == "__main__":
    main()
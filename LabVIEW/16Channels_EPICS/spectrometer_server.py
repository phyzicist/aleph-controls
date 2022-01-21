from pvaccess import INT
from pvaccess import FLOAT
from pvaccess import STRING
from pvaccess import PvObject
from pvaccess import PvaServer
# import matplotlib.pyplot as plt
import os
import sys
import time
from seabreeze.spectrometers import Spectrometer,list_devices

def GetNewData(count0):

	wavelengths,intensities = spec.spectrum()
	count0=count0+1
	# print('Get #'+ str(count0)+' spectrum')

	return count0,wavelengths,intensities
	
if __name__=='__main__':
	
	pv=PvObject({'a':STRING,'b':[FLOAT], 'c':[FLOAT], 'd':INT, 'e':STRING})
	server=PvaServer('spectrum',pv)

	oldfilename=None
	Date=20000101
	shotnumber=0
	devices = list_devices()
	print(devices)
	# spec = Spectrometer.from_first_available()
	spec = Spectrometer.from_serial_number("USB4C00491")

	spec.trigger_mode(2) #0: Free running, 1: software trigger, 2: external level trigger, 3:shutter mode
	spec.integration_time_micros(100000)  # 0.1 seconds

	while True:
		OldDate=Date
		datetime=time.strftime('%Y%m%d-%H_%M_%S')
		Date=datetime.split('-')[0]
		Time=datetime.split('-')[1]
		if OldDate!=Date:
			shotnumber=0
		shotnumber,wavelengths,intensities=GetNewData(shotnumber)
		wavelength=wavelengths.tolist()
		intensity=intensities.tolist()
		# plt.plot(wavelength,intensity)
		# plt.pause(0.001)


		# print(wavelength)
		pv.set({'a':Date})
		pv.set({'b':wavelength})
		pv.set({'c':intensity})
		pv.set({'d':shotnumber})
		pv.set({'e':Time})
		server.update('spectrum',pv)
		print('Data sent!'+'@'+Date+' '+Time)

		time.sleep(0.5)
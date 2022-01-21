from pvaccess import Channel
from pvaccess import PVA
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
from os import path, getcwd, makedirs
import numpy as np


n=1  # save file every n shot
shotnumber=0
# count=-1   # count for waiting time

#####
fig1= plt.figure(figsize=(4, 3))
wavelegnth=[]
intensity_au=[]
Plot1 = fig1.add_subplot()
# Plot1.set_xlabel('Wavelength / nm',fontsize=11,color='black')
# Plot1.set_ylabel('Intensity / a.u.',fontsize=11,color='black')
Plot1.set_title('Spectrum \n Intensity(a.u.) vs Wavelength(nm)',fontweight='bold',fontsize =10)
Plot1.set_xlim(780, 830)
Plot1.set_ylim(0,1)
line, = Plot1.plot(wavelegnth, intensity_au, 'r')
#####

def getdata():
	channelName='spectrum'
	channel = Channel(channelName,PVA)
	# pv=channel.get('field(b)')
	pv = channel.get()
	# print(pv)
	Date=pv['a']
	wavelength=pv['b']
	intensity=pv['c']
	shotnumber=pv['d']
	Time=pv['e']

	return Date,wavelength, intensity, shotnumber, Time

def create_csv(Date,Time,shotnumber,wavelength,intensity):
	dirs=path.join(getcwd(),Date)
	if not path.exists(dirs):
		makedirs(dirs)
	filename = path.join(dirs,Date+'_'+Time+'.csv')
	dataframe = pd.DataFrame({'Wavelength/nm':wavelength,'Intensity':intensity})
	dataframe.to_csv(filename,index=False,sep=',')


def Plotdata(shotnumber):
	# ,count):
	# for x in range(1000):
	oldshotnumber=shotnumber
	Date,wavelength,intensity,shotnumber,Time=getdata()
	# print(shotnumber)
	# print(oldshotnumber)
	if shotnumber>oldshotnumber: 
		if shotnumber%n==0:
			create_csv(Date,Time,shotnumber,wavelength,intensity)
		

		##### Code opening figure and displaying data
		intensity_au=[]
		wavelength_temp=[]

		## wavelength=wavelength.tolist()
		## print(type(wavelength))

		index1=np.where(wavelength<900)[0]   # set wavelength limit
		index2=np.where(wavelength>700)[0]   # set wavelength limit

		## print(index2)

		maxvalue=max(intensity[min(index2):max(index1)])
		minvalue=min(intensity[min(index2):max(index1)])

		## print(max(index2))

		i=min(index2)
		while i<max(index1):
			wavelength_temp.append(wavelength[i])
			intensity_au.append((intensity[i]-minvalue)/(maxvalue-minvalue))   # Normalize Intensity
			i=i+1

		## ii =0
		## while ii<len(wavelength):
		## 	wavelength_temp.append(wavelength[ii])
		## 	intensity_au.append((intensity[ii]-min(intensity))/(max(intensity)-min(intensity)))   # Normalize Intensity
		## 	ii=ii+1


		## print(wavelength_temp)

		line.set_data(wavelength_temp, intensity_au)
		print('Data received @' +Date +' '+ Time + ' shot #: '+ str(shotnumber))

		## count=-1

		plt.pause(0.01)
		#####

	return shotnumber
	# ,count

if __name__=='__main__':

	while True:
		# shotnumber,count=Plotdata(shotnumber,count)
		shotnumber=Plotdata(shotnumber)


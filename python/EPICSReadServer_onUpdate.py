import time
import epics
from epics import PV

#address's of shared variables
base_address="ALEPH-WORKSTATION-01:server_library:"
#base_address="DESKTOP-73SSMS3:server_lib:"
timeStamp_address=base_address+"timeStamp.VAL"
frontend1_address=base_address+"frontend1.VAL"
frontend2_address=base_address+"frontend2.VAL"
QuantaRay_address=base_address+"QuantaRay.VAL"
slab2_address=base_address+"slab2.VAL"
slab3_address=base_address+"slab3.VAL"
slab4_address=base_address+"slab4.VAL"
slab5_address=base_address+"slab5.VAL"
slab7_address=base_address+"slab7.VAL"
slab8_address=base_address+"slab8.VAL"
slab9_address=base_address+"slab9.VAL"
slab10_address=base_address+"slab10.VAL"
stage1_address=base_address+"stage1.VAL"
stage2_address=base_address+"stage2.VAL"
stage3_address=base_address+"stage3.VAL"
stage4_address=base_address+"stage4.VAL"
stage5_address=base_address+"stage5.VAL"

#Local Variables
timeStamp=""
frontend1=0
frontend2=0
QuantaRay=0
slab2=0
slab3=0
slab4=0
slab5=0
slab7=0
slab8=0
slab9=0
slab10=0
stage1=0
stage2=0
stage3=0
stage4=0
stage5=0


#Callback to print name and value when any value is updated
def valueUpdatedCallback(value=None,pvname=None, **kw):
	global base_address
	print("Name:%s | Value:%f" % (pvname[len(base_address):-4],  value))

#Callback for timeStamp update
def timeStampCallback(value=None,pvname=None, **kw):
	global base_address
	global timeStamp
	timeStamp=value
	print("Name:%s | Value:%s" % (pvname[len(base_address):-4],  value))

#Callback for frontend1 update
def frontend1Callback(value=None, **kw):
	global frontend1
	frontend1=value

#Callback for frontend2 update
def frontend2Callback(value=None, **kw):
	global frontend2
	frontend2=value

#Callback for QuantaRay update
def QuantaRayCallback(value=None, **kw):
	global QuantaRay
	QuantaRay=value

#Callback for slab2 update
def slab2Callback(value=None, **kw):
	global slab2
	slab2=value

#Callback for slab3 update
def slab3Callback(value=None, **kw):
	global slab3
	slab3=value

#Callback for slab4 update
def slab4Callback(value=None, **kw):
	global slab4
	slab4=value

#Callback for slab5 update
def slab5Callback(value=None, **kw):
	global slab5
	slab5=value

#Callback for slab7 update
def slab7Callback(value=None, **kw):
	global slab7
	slab7=value

#Callback for slab8 update
def slab8Callback(value=None, **kw):
	global slab8
	slab8=value

#Callback for slab9 update
def slab9Callback(value=None, **kw):
	global slab9
	slab9=value

#Callback for slab10 update
def slab10Callback(value=None, **kw):
	global slab10
	slab10=value

#Callback for stage1 update
def stage1Callback(value=None, **kw):
	global stage1
	stage1=value

#Callback for stage2 update
def stage2Callback(value=None, **kw):
	global stage2
	stage2=value

#Callback for stage3 update
def stage3Callback(value=None, **kw):
	global stage3
	stage3=value

#Callback for stage4 update
def stage4Callback(value=None, **kw):
	global stage4
	stage4=value

#Callback for stage5 update
def stage5Callback(value=None, **kw):
	global stage5
	stage5=value


#Connect process variables
#Configured to call both the specific and the general callback functions when the value of the variable is updated
timeStamp_pv=PV(timeStamp_address, callback=timeStampCallback)
frontend1_pv=PV(frontend1_address, callback=(frontend1Callback,valueUpdatedCallback))
frontend2_pv=PV(frontend2_address, callback=(frontend2Callback,valueUpdatedCallback))
QuantaRay_pv=PV(QuantaRay_address, callback=(QuantaRayCallback,valueUpdatedCallback))
slab2_pv=PV(slab2_address, callback=(slab2Callback,valueUpdatedCallback))
slab3_pv=PV(slab3_address, callback=(slab3Callback,valueUpdatedCallback))
slab4_pv=PV(slab4_address, callback=(slab4Callback,valueUpdatedCallback))
slab5_pv=PV(slab5_address, callback=(slab5Callback,valueUpdatedCallback))
slab7_pv=PV(slab7_address, callback=(slab7Callback,valueUpdatedCallback))
slab8_pv=PV(slab8_address, callback=(slab8Callback,valueUpdatedCallback))
slab9_pv=PV(slab9_address, callback=(slab9Callback,valueUpdatedCallback))
slab10_pv=PV(slab10_address, callback=(slab10Callback,valueUpdatedCallback))
stage1_pv=PV(stage1_address, callback=(stage1Callback,valueUpdatedCallback))
stage2_pv=PV(stage2_address, callback=(stage2Callback,valueUpdatedCallback))
stage3_pv=PV(stage3_address, callback=(stage3Callback,valueUpdatedCallback))
stage4_pv=PV(stage4_address, callback=(stage4Callback,valueUpdatedCallback))
stage5_pv=PV(stage5_address, callback=(stage5Callback,valueUpdatedCallback))


#length of time in s to continue checking values
runtime=2
t0=time.time()
while time.time()-t0<runtime:
	time.sleep(1.e-3)
print("done")

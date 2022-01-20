import time
import epics
from epics import PV

#Variables
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

#Connect process variables
timeStamp_pv=PV(timeStamp_address)
frontend1_pv=PV(frontend1_address)
frontend2_pv=PV(frontend2_address)
QuantaRay_pv=PV(QuantaRay_address)
slab2_pv=PV(slab2_address)
slab3_pv=PV(slab3_address)
slab4_pv=PV(slab4_address)
slab5_pv=PV(slab5_address)
slab7_pv=PV(slab7_address)
slab8_pv=PV(slab8_address)
slab9_pv=PV(slab9_address)
slab10_pv=PV(slab10_address)
stage1_pv=PV(stage1_address)
stage2_pv=PV(stage2_address)
stage3_pv=PV(stage3_address)
stage4_pv=PV(stage4_address)
stage5_pv=PV(stage5_address)

#get variabe values
timeStamp=timeStamp_pv.get()
frontend1=frontend1_pv.get()
frontend2=frontend2_pv.get()
QuantaRay=QuantaRay_pv.get()
slab2=slab2_pv.get()
slab3=slab3_pv.get()
slab4=slab4_pv.get()
slab5=slab5_pv.get()
slab7=slab7_pv.get()
slab8=slab8_pv.get()
slab9=slab9_pv.get()
slab10=slab10_pv.get()
stage1=stage1_pv.get()
stage2=stage2_pv.get()
stage3=stage3_pv.get()
stage4=stage4_pv.get()
stage5=stage5_pv.get()

print("timeStamp:%s"%timeStamp)
print("frontend1:%f"%frontend1)
print("frontend2:%f"%frontend2)
print("QuantaRay:%f"%QuantaRay)
print("slab2:%f"%slab2)
print("slab3:%f"%slab3)
print("slab4:%f"%slab4)
print("slab5:%f"%slab5)
print("slab7:%f"%slab7)
print("slab8:%f"%slab8)
print("slab9:%f"%slab9)
print("slab10:%f"%slab10)
print("stage1:%f"%stage1)
print("stage2:%f"%stage2)
print("stage3:%f"%stage3)
print("stage4:%f"%stage4)
print("stage5:%f"%stage5)

#!/usr/bin/env python

import argparse
from siriuspy.magnet.factory import NormalizerFactory
from siriuspy.search import MASearch
# Import the basic framework components.
from softioc import softioc, builder
import cothread
from cothread.catools import caget, caput, camonitor

# Parse command line arguments
parser = argparse.ArgumentParser(description='Start an EPICS IOC with the specified for specific sector number')
parser.add_argument('sector', type=str, help='Sector number')
args = parser.parse_args()

print(args.sector)
# Define the name of the device you want to convert
sector = args.sector

correctors = ['M1', 'M2', 'C2', 'C3']
orientation= ['FCH', 'FCV']

# get dipole energy, used for conversions
dipole_strength = 3  # GeV, read from PV SI-Fam:PS-B1B2-1:EnergyRef-Mon

Kick_RB = []
KickRef_Mon = []
KickAcc_Mon = []
Kick_Mon = []
Kick_SP = []
Current_RB = []
CurrentRef_Mon = []
FOFBAcc_Mon = []
Current_Mon = []

for corr in correctors:
    for ori in orientation:
        psname = 'SI-'+sector+corr+':PS-'+ori

        # get the name of the respective magnet
        maname = MASearch.conv_psname_2_psmaname(psname)

        # create normalizer object
        norm = NormalizerFactory.create(maname)

        # Create some records
        Kick_RB.append(builder.aIn(psname+':Kick-RB'))
        KickRef_Mon.append(builder.aIn(psname+':KickRef-Mon'))
        KickAcc_Mon.append(builder.aIn(psname+':KickAcc-Mon'))
        Kick_Mon.append(builder.aIn(psname+':Kick-Mon'))

        Kick_SP.append(builder.aOut(psname+':Kick-SP', on_update=lambda v: caput(psname + ':Current-SP', norm.conv_strength_2_current(v, strengths_dipole=dipole_strength))))

        Current_RB.append(psname+':Current-RB')
        CurrentRef_Mon.append(psname+':CurrentRef-Mon')
        FOFBAcc_Mon.append(psname+':FOFBAcc-Mon')
        Current_Mon.append(psname+':Current-Mon')

# Boilerplate get the IOC started
builder.LoadDatabase()
softioc.iocInit()

def rb(val,index):
    Kick_RB[index].set(norm.conv_current_2_strength(val, strengths_dipole=dipole_strength))
def ref_mon(val,index):
    KickRef_Mon[index].set(norm.conv_current_2_strength(val, strengths_dipole=dipole_strength))
def acc_mon(val,index):
    KickAcc_Mon[index].set(norm.conv_current_2_strength(val, strengths_dipole=dipole_strength))
def mon(val,index):
    Kick_Mon[index].set(norm.conv_current_2_strength(val, strengths_dipole=dipole_strength))


camonitor(Current_RB, rb)
camonitor(CurrentRef_Mon, ref_mon)
camonitor(FOFBAcc_Mon, acc_mon)
camonitor(Current_Mon, mon)

# Finally leave the IOC running with an interactive shell.
softioc.interactive_ioc(globals())


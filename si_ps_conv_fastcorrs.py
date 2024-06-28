#!/usr/bin/env python

import argparse
from siriuspy.magnet.factory import NormalizerFactory
from siriuspy.search import MASearch
# Import the basic framework components.
from softioc import softioc, builder
import cothread
from cothread.catools import caget, caput

# Parse command line arguments
parser = argparse.ArgumentParser(description='Start an EPICS IOC with the specified PS name.')
parser.add_argument('psname', type=str, help='The name of the power supply (PS) device')
args = parser.parse_args()

print(args.psname)
# Define the name of the device you want to convert
psname = args.psname[:-1]
# Set the record prefix
builder.SetDeviceName('my-'+psname)

# get the name of the respective magnet
maname = MASearch.conv_psname_2_psmaname(psname)

# create normalizer object
norm = NormalizerFactory.create(maname)

# get dipole energy, used for conversions
dipole_strength = 3  # GeV, read from PV SI-Fam:PS-B1B2-1:EnergyRef-Mon

# Create some records
Kick_RB = builder.aIn('Kick-RB')
KickRef_Mon = builder.aIn('KickRef-Mon')
KickAcc_Mon = builder.aIn('KickAcc-Mon')
Kick_Mon = builder.aIn('Kick-Mon')

# Correct the string concatenation
Kick_SP = builder.aOut('Kick-SP', on_update=lambda v: caput(psname + ':Current-SP', norm.conv_strength_2_current(v, strengths_dipole=dipole_strength)))

# Boilerplate get the IOC started
builder.LoadDatabase()
softioc.iocInit()

# Start processes required to be run after iocInit
def update():
    while True:
        Kick_RB.set(norm.conv_current_2_strength(caget(psname + ':Current-RB'), strengths_dipole=dipole_strength))
        KickRef_Mon.set(norm.conv_current_2_strength(caget(psname + ':CurrentRef-Mon'), strengths_dipole=dipole_strength))
        KickAcc_Mon.set(norm.conv_current_2_strength(caget(psname + ':FOFBAcc-Mon'), strengths_dipole=dipole_strength))
        Kick_Mon.set(norm.conv_current_2_strength(caget(psname + ':Current-Mon'), strengths_dipole=dipole_strength))

cothread.Spawn(update)

# Finally leave the IOC running with an interactive shell.
softioc.interactive_ioc(globals())


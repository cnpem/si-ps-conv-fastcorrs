#!/usr/bin/env python

import argparse
from siriuspy.magnet.factory import NormalizerFactory
from siriuspy.search import MASearch
from softioc import softioc, builder
from softioc.builder import records
from cothread.catools import caput

# Parse command line arguments
parser = argparse.ArgumentParser(description='Start an EPICS IOC for a specific sector number')
parser.add_argument('sector', type=str, help='Sector number')
args = parser.parse_args()

print(args.sector)
sector = args.sector

correctors = ['M1', 'M2', 'C2', 'C3']
orientation = ['FCH', 'FCV']

# Get dipole energy, used for conversions
dipole_strength = 3  # GeV, read from PV SI-Fam:PS-B1B2-1:EnergyRef-Mon

# Dictionary to store records and normalizers
records_dict = {}

for corr in correctors:
    for ori in orientation:
        psname = 'SI-' + sector + corr + ':PS-' + ori

        # Get the name of the respective magnet
        maname = MASearch.conv_psname_2_psmaname(psname)

        # Create normalizer object
        norm = NormalizerFactory.create(maname)

        # Initialize or update the dictionary for this psname
        if psname not in records_dict:
            records_dict[psname] = {}

        # Add the normalizer object
        records_dict[psname]['norm'] = norm

        # Create and populate records in the dictionary without overwriting
        records_dict[psname]['kick_rb'] = builder.aIn('my-' + psname + ':Kick-RB')
        records_dict[psname]['current_rb'] = records.ai('my-' + psname + ':Current-RB', INP='sim-' + psname + ':Current-RB CP')
        records_dict[psname]['fwd_rb'] = records.ao(psname + ':Fwd-RB', OMSL='closed_loop', DOL='my-' + psname + ':Current-RB CP', OUT=psname + ':Conv-RB PP')
        records_dict[psname]['conv_rb'] = builder.aOut(psname + ':Conv-RB', always_update=True,
                                                       on_update=lambda v, psname=psname:
                                                       records_dict[psname]['kick_rb'].set(
                                                           records_dict[psname]['norm'].conv_current_2_strength(v, strengths_dipole=dipole_strength))
                                                       )

        # Add KickRef-Mon, CurrentRef-Mon, and FwdRef-Mon records
        records_dict[psname]['kickRef_mon'] = builder.aIn('my-' + psname + ':KickRef-Mon')
        records_dict[psname]['currentRef_mon'] = records.ai('my-' + psname + ':CurrentRef-Mon', INP='sim-' + psname + ':CurrentRef-Mon CP')
        records_dict[psname]['fwdRef_mon'] = records.ao(psname + ':FwdRef-Mon', OMSL='closed_loop', DOL='my-' + psname + ':CurrentRef-Mon CP', OUT=psname + ':ConvRef-Mon PP')
        records_dict[psname]['convRef_mon'] = builder.aOut(psname + ':ConvRef-Mon', always_update=True,
                                                       on_update=lambda v, psname=psname:
                                                       records_dict[psname]['kickRef_mon'].set(
                                                           records_dict[psname]['norm'].conv_current_2_strength(v, strengths_dipole=dipole_strength))
                                                       )

        # Add KickAcc-Mon, FOFBAcc-Mon, and FwdAcc-Mon records
        records_dict[psname]['kickAcc_mon'] = builder.aIn('my-' + psname + ':KickAcc-Mon')
        records_dict[psname]['fofbAcc_mon'] = records.ai('my-' + psname + ':FOFBAcc-Mon', INP='sim-' + psname + ':FOFBAcc-Mon CP')
        records_dict[psname]['fwdAcc_mon'] = records.ao(psname + ':FwdAcc-Mon', OMSL='closed_loop', DOL='my-' + psname + ':FOFBAcc-Mon CP', OUT=psname + ':ConvAcc-Mon PP')
        records_dict[psname]['convAcc_mon'] = builder.aOut(psname + ':ConvAcc-Mon', always_update=True,
                                                       on_update=lambda v, psname=psname:
                                                       records_dict[psname]['kickAcc_mon'].set(
                                                           records_dict[psname]['norm'].conv_current_2_strength(v, strengths_dipole=dipole_strength))
                                                       )

        # Add Kick-Mon, FOFB-Mon, and Fwd-Mon records
        records_dict[psname]['kick_mon'] = builder.aIn('my-' + psname + ':Kick-Mon')
        records_dict[psname]['fofb_mon'] = records.ai('my-' + psname + ':Current-Mon', INP='sim-' + psname + ':Current-Mon CP')
        records_dict[psname]['fwd_mon'] = records.ao(psname + ':Fwd-Mon', OMSL='closed_loop', DOL='my-' + psname + ':Current-Mon CP', OUT=psname + ':Conv-Mon PP')
        records_dict[psname]['conv_mon'] = builder.aOut(psname + ':Conv-Mon', always_update=True,
                                                       on_update=lambda v, psname=psname:
                                                       records_dict[psname]['kick_mon'].set(
                                                           records_dict[psname]['norm'].conv_current_2_strength(v, strengths_dipole=dipole_strength))
                                                       )

        # Add Kick-SP record
        records_dict[psname]['kick_sp'] = builder.aOut('my-'+psname+':Kick-SP', always_update=True,
                                                       on_update=lambda v, psname=psname:
                                                       records_dict[psname]['current_sp'].set(
                                                           records_dict[psname]['norm'].conv_strength_2_current(v, strengths_dipole=dipole_strength))
                                                       )

        # Auxiliary record for the setpoint, using ao with OUT and DOL fields
        records_dict[psname]['current_sp'] = records.ao('my-'+psname+':Current-SP',
                                                    OUT=psname+':Current-SP PP')

# Boilerplate to get the IOC started
builder.LoadDatabase()
softioc.iocInit()

# Finally, leave the IOC running with an interactive shell.
softioc.interactive_ioc(globals())

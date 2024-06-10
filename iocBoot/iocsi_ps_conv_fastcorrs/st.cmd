#!../../bin/linux-x86_64/si_ps_conv_fastcorrs

#- You may have to change si_ps_conv_fastcorrs to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/si_ps_conv_fastcorrs.dbd"
si_ps_conv_fastcorrs_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/cntrec.db","user=gustavoreis")
dbLoadRecords("db/kicks.db","user=gustavoreis, P=$(P), R=$(R)")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=gustavoreis"

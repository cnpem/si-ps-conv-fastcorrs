#!../../bin/linux-x86_64/si_ps_conv_fastcorrs

< envPaths
epicsEnvSet("CALC","/home/ABTLUS/gustavo.reis/EPICS/support/calc")
cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/si_ps_conv_fastcorrs.dbd"
si_ps_conv_fastcorrs_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("db/dipole.db","user=gustavoreis, SEC=$(SEC)")
dbLoadRecords("db/machine_params.db")

cd "${TOP}/iocBoot/${IOC}"
iocInit

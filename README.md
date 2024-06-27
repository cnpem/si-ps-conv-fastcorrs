O módulo PythonSoftIOC permite que uma IOC EPICS seja escrita em um script Python
e executada de um interpretador. Além disso, possui em sua própria biblioteca a
implementação de links Channel Access, importantes para ler e escrever valores
de PVs externas.
Não necessita de nenhum módulo que dê suporte à EPICS instalado, além da própria
lib Python PythonSoftIOC.

```
usage: si_ps_conv_fastcorrs.py [-h] psname

Start an EPICS IOC with the specified PS
name.

positional arguments:
  psname      The name of the power supply
              (PS) device

optional arguments:
  -h, --help  show this help message and
              exit
```

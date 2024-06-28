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

Resultado do comando `htop` filtrando o `si_ps_conv_fastcorrs.py`:
```
    PID USER       PRI  NI  VIRT   RES   SHR S  CPU%▽MEM%   TIME+  Command
 311888 gustavo.re  20   0 2078M 93612 34576 R  47.1  1.2  7:25.05 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311905 gustavo.re  20   0 2078M 93612 34576 S   8.4  1.2  1:21.78 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311926 gustavo.re  20   0 2078M 93612 34576 S   3.9  1.2  0:42.22 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311927 gustavo.re  20   0 2078M 93612 34576 S   2.6  1.2  0:23.30 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311898 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311899 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311900 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311901 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.82 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311902 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311903 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311904 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311906 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311907 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311908 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311909 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311910 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.02 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311911 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311912 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311913 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311914 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311915 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311916 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.01 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311917 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.02 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311918 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.05 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311919 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.10 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311920 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311921 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311922 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311923 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311924 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 311925 gustavo.re  20   0 2078M 93612 34576 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
```

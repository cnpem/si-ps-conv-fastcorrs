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
 257161 gustavo.re  20   0 1874M 95448 35236 S   0.7  1.2  0:02.02 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257159 gustavo.re  20   0  2580   912   812 S   0.0  0.0  0:00.00 /bin/sh -c ./si_ps_conv_fastcorrs.py ${P}${R}
 257173 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257174 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257175 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257176 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.17 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257178 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257179 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257180 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257181 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257182 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257183 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257184 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257185 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257186 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257187 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257188 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257189 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257190 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257191 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257192 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257193 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257194 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.01 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257195 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.01 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257196 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257197 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257198 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257199 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257200 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257201 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 257203 gustavo.re  20   0 1874M 95448 35236 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
```

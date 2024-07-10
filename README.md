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
 440670 gustavo.re  20   0 2079M 93048 34000 S   0.6  1.2  0:07.21 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440687 gustavo.re  20   0 2079M 93048 34000 S   0.6  1.2  0:00.69 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 441292 gustavo.re  20   0 2079M 93048 34000 S   0.6  1.2  0:00.34 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440680 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440681 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440682 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440683 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:01.53 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440684 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440685 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440686 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440688 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440689 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440690 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440691 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440692 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.02 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440693 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440694 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440695 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440696 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440697 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440698 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.01 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440699 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.03 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440700 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.08 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440701 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.15 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440702 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440703 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440704 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440705 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440706 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440707 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440708 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.73 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 440709 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
 441293 gustavo.re  20   0 2079M 93048 34000 S   0.0  1.2  0:00.00 python ./si_ps_conv_fastcorrs.py SI-01M2:PS-FCH:
```

Jitter médio entre monitoramento de corrente e monitoramento de kicks: 0.42ms

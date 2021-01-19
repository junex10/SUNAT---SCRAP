import time
import re
import subprocess

x = 0

while(x != 1):
    tmp = 0
    print('Elige el mes')

    tmp = input()
    if (tmp == '1'):
        subprocess.Popen(['python', 'enero.py'])
    if(tmp == '2'):
        subprocess.Popen(['python', 'febrero.py'])
    if(tmp == '3'):
        subprocess.Popen(['python', 'marzo.py'])
    if(tmp == '4'):
        subprocess.Popen(['python', 'abril.py'])
    if(tmp == '5'):
        subprocess.Popen(['python', 'mayo.py'])
    if(tmp == '6'):
        subprocess.Popen(['python', 'junio.py'])
    if(tmp == '7'):
        subprocess.Popen(['python', 'julio.py'])
    if(tmp == '8'):
        subprocess.Popen(['python', 'agosto.py'])
    if(tmp == '9'):
        subprocess.Popen(['python', 'septiembre.py'])
    if(tmp == '10'):
        subprocess.Popen(['python', 'octubre.py'])
    if(tmp == '11'):
        subprocess.Popen(['python', 'noviembre.py'])
    if(tmp == '12'):
        subprocess.Popen(['python', 'diciembre.py'])
    x = 1
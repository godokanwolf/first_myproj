import subprocess
from time import sleep
import os


wichi = 'c:\\test\\unilog32.txt'

current_machine_id = subprocess.check_output(
    'wmic csproduct get uuid').decode().split('\n')[0].strip()
print(current_machine_id)
with open(wichi, 'w') as f:
    f.write(current_machine_id)
    sleep(2)
    isfl = os.path.isfile(wichi)

if isfl:
    print('Sucess!')
    sleep(2)

else:
    print('Falid')
    sleep(2)

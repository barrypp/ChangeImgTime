import os
import re
import time
from pathlib import Path

info = re.compile('Blame([0-9]+)-([0-9]+)')
p = Path('data')

for x in p.iterdir():
    #
    i = info.match(x.name)
    hour = int(i.group(1))
    num = int(i.group(2))
    #
    t = time.mktime((2019,1,8,hour,0,num,0,0,-1))
    os.utime(x,(t,t))
    print(x.name)

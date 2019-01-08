import os
import re
import time
from datetime import datetime, timedelta
from pathlib import Path

import piexif

info = re.compile('Blame([0-9]+)-([0-9]+)')
p = Path('data')

for x in p.iterdir():
    #
    i = info.match(x.name)
    hour = int(i.group(1))
    num = int(i.group(2))
    #
    t = datetime(2019,1,8,hour) + timedelta(0,num)
    os.utime(x,(t.timestamp(),t.timestamp()))
    #
    if x.suffix == '.jpg':
        exif_dict = piexif.load(str(x))
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = t.strftime('%Y:%m:%d %H:%M:%S')
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = t.strftime('%Y:%m:%d %H:%M:%S')
        piexif.insert(piexif.dump(exif_dict), str(x))
    #
    print(x.name)

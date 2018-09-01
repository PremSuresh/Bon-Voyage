import glob
import time
from importlib import reload
from urllib.request import urlopen
import cv2
import numpy as np
import os

url = 'http://172.17.105.140:8080/shot.jpg'
i = 0
a = len(glob.glob('images_1'))
while a < 600:
    print(a)
    imgResp = urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('test', img)
    cv2.imwrite('images_1\pic{:>05}.png'.format(i), img)
    a += 1
    i += 1

    if ord('q') == cv2.waitKey(10):
        exit(0)
else:
    cv2.waitKey(10)
    import vid2
    reload(vid2)
    mydir = 'images_1'
    filelist = [f for f in os.listdir(mydir) if f.endswith(".png")]
    print("REMOVING FILES")
    time.sleep(5)
    for f in filelist:
        os.remove(os.path.join(mydir, f))


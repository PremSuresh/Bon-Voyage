from importlib import reload
t = 0
import vid
while t<10:
    reload(vid)
    t+=1

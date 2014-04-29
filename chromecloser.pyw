import subprocess
import time
from random import randrange 
#creating a forever loop
while True :
    time.sleep(randrange(1,3000))
    #for testing# time.sleep(randrange(1,10))
    subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
    #time.sleep(randrange(1,3000))
        
        

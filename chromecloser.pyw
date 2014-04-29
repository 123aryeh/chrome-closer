import os
import time
from random import randrange 
#creating a forever loop
while True :
    
    time.sleep(randrange(1,10))
    os.system("TASKKILL /F /IM chrome.exe")
    #time.sleep(randrange(1,90))
    
        
        

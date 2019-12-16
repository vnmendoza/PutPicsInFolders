import os
from os import listdir
from os.path import isfile, join
import fnmatch
import shutil

#dir = os.path.join("Z:\\Clients\\Engineering Assoc - MCI\\Hubs\\Inglewood\\3 - Aerial\\Photos\\IGW_2\\IGW_2.2","newPath")
dir = os.path.join("C:\\Users\\vmend\\Desktop","newPath")
if not os.path.exists(dir):
    os.mkdir(dir)
onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
folderNames = []
for item in onlyfiles:
    folderNames.append(item.split('-')[0])
   
print("`````````````````````````")
for file in folderNames:
    picFolder = os.path.join(dir, file)
    if not os.path.exists(picFolder):
        os.mkdir(picFolder)
    for f in os.listdir(dir):
        if fnmatch.fnmatch(f,(file + "*.jpg")):
            shutil.move((dir + "\\" + f),picFolder)
                           
        

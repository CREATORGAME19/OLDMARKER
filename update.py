import os
import urllib.request
f = open("MARKER.py","w")
f.close()
os.remove("MARKER.py")
data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/MARKER.py","MARKER.py")
print(os.system('MARKER.py'))
print("Done!")
os.remove("temp_update.py")

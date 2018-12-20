import os
import urllib.request
os.remove("MARKER.py")
data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/MARKER.py","MARKER.py")
print(os.system('MARKER.py'))
print("Done!")

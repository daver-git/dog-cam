#!/usr/bin/python3
# Time lapse dog walk cam on RasPi Zero
import os
from datetime import datetime
from time import sleep
import subprocess
import picamera

cwd = os.getcwd() # Current Working Dir
# Get SSID to derermine when mobile
ssidOld = "NoSSID"
#sidNew = ""
# Read mobile SSID from file
try:
    with open(cwd + '/ssidMob','r') as ssidMob:
        ssidMob = (ssidMob.read().rstrip())
except:
    ssidMob = "NoSSID"

# Define static HTML
htmlHead = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN">
<html>
  <head>
    <title>Dog Walk Camera Monitor</title>
  </head>
  <body>
    <img src="/icons/openlogo-75.png" alt="Debian Logo">
"""
htmlTail = """
  </body>
</html>
"""

dt = ""
tm = ""
dttm = ""

def Get_DtTm():
    global dt
    global tm
    global dttm
    today = datetime.today()
    dt = today.strftime('%Y-%m-%d')
    tm = today.strftime('%H:%M:%S')
    dttm = dt + " " + tm

def Do_Cam():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # Hi Res
        camera.resolution = (640, 480) # Lo Res
        sleep (2)
        Get_DtTm()
        camera.capture(pixDir + '/img' + tm.replace(":", "") + '.jpg')
        camera.close()
        
#need to def main!!!
#but will vars be global?

Get_DtTm()
pixDir = cwd + "/pix/" + dt
log = open(cwd + "/cam.log","a+", newline=None)
if not os.path.exists(pixDir): # Create target dir(s)
    os.makedirs(pixDir)
    print("py+ " + dttm + " " + pixDir, file=log)
else:
    print("py+ " + dttm, file=log)

# Main Loop ======================================================================
cnt = 0
while True:
    if (cnt == 0):
# Check if SSID changed every 10 pics
        cnt = 10
        ssidNew = (subprocess.run(["iwgetid", "--raw"], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip())
        if ssidNew != ssidOld:
            ssidOld = ssidNew
            print ("py, " + dttm + " SSID = " + ssidNew, file=log)
#   if (ssidNew == ssidMob): # We are on mobile WiFi
# Do it anyway while testing
    Do_Cam()
    cnt -= 1
# Write HTML
    html = "<p>Dog Walk Camera Monitor</p>"
    html = html + "Last image capture: " + dttm + "<br>"
    with open("/var/www/html/index.html", "w") as htmlFile:
        htmlFile.write(htmlHead + html + htmlTail)
# Terminate background process
    if os.path.exists(cwd + "/stop"):
        os.remove(cwd + "/stop")
        break

# Main Loop End ==================================================================
#
#   top = subprocess.run(["top", "-b", "-n1"], stdout=subprocess.PIPE).stdout.decode('utf-8')
#   print(top) # need head -5

# Exit
Get_DtTm()
print ("py- " + dttm, file=log)
log.close()


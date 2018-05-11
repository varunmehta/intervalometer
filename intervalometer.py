# Run the file on boot;
#
# nano /etc/crontab
# @reboot root /path/to/script.sh
#

from picamera import PiCamera
from time import sleep
import time
import os

# Purpose of this program is to keep clicking photos,
# till storage is full or the pi is unplugged.
camera = PiCamera()
FILE_PATH='/data'

# create dir first time
# if not os.path.exists(FILE_PATH):
#    os.makedirs(FILE_PATH)

print ("Program started")

# initalize camera
camera.start_preview()
print ("now sleeping... ")
sleep(10)

# infinite loop to click pictures
while True:
    file_name = int(round(time.time()))
    print ("Filename: " + file_name)
    camera.capture(FILE_PATH + '/' + file_name + '.jpg')
    # click a picture every 5 seconds.

    print ("Captured, now sleeping...")
    sleep(5)
camera.stop_preview()
print ("Program exited")

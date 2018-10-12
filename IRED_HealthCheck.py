# IRED Health check module

import IRED_Logger
import subprocess
import time
import re

def getCurrTemp():
   logger = IRED_Logger.get_logger_instance()
   commandResponse = subprocess.check_output(["vcgencmd","measure_temp"])
   logger.info ("getCurrTemp - {}".format(commandResponse))
   c = re.findall("\d+\.\d+", commandResponse)
#c = float(commandResponse.strip()[-1]) #-- Removes the final CR character and gets only the "0" or "1" from detected status
#   logger.info ("getCurrTemp - ", c)
   return c

def getCameraStatus():
   logger = IRED_Logger.get_logger_instance()
   commandResult = subprocess.check_output("vcgencmd get_camera", shell=True)
   logger.info ("getCameraStatus - {}".format(commandResult))  
   c = int(commandResult.strip()[-1]) #-- Removes the final CR character and gets only the "0" or "1" from detected status
   #logger.info ("getCameraStatus - {}".format(c))  
   if (c):
      logger.info ("Camera detected")
      return 1
   else:
      logger.info ("Camera not detected")
      return 0


def getDeviceStatus():
    curr_temp = getCurrTemp()
    cam_det = getCameraStatus()
    return 1


if __name__ == "__main__":
    getDeviceStatus()
